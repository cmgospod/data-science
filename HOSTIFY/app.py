from flask import Flask, render_template, request
from joblib import load
import pandas as pd
import json

pipeline = load('MODEL/model.joblib')


def create_app():
    """Create and configure a basic Flask app"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('base.html')

    @app.route('/input', methods=['POST'])
    def retrieval():
        try:
            requestJson = json.loads(request.data)
            neighbourhood_group = int(requestJson['neighborhood_group'])
            neighbourhood = int(requestJson['neighborhood'])
            room_type = int(requestJson['room_type'])
            minimum_nights = int(requestJson['minimum_nights'])
            calculated_host_listings_count = int(
                requestJson['calculated_host_listings_count'])
            availability_365 = int(requestJson['availability_of_year'])
            bathrooms = int(requestJson['bathroom_number'])
            bedrooms = int(requestJson['bedroom_number'])
            predict_thing = pd.DataFrame(
                columns=['neighbourhood_group', 'neighbourhood', 'room_type',
                         'minimum_nights', 'calculated_host_listings_count',
                         'availability_365', 'bathrooms', 'bedrooms'],
                data=[[neighbourhood_group, neighbourhood, room_type,
                      minimum_nights, calculated_host_listings_count,
                      availability_365, bathrooms, bedrooms]]
                )
            prediction = int(pipeline.predict(predict_thing)[0].round())
            # The Mean Absolute Error (MAE) is 19
            # The Mean Absolute Percentage Error (MAPE) is 36.62%
            # Use MAPE for low predicted prices and MAE for higher prices
            error = prediction*.3662 if prediction*.3662 < 19 else 19
            low_range = round(prediction-error)
            if low_range < 1:
                low_range = 1
            high_range = round(prediction+error)
            price_range = 'Predicted price range for your listing is: '
            return price_range + f'€{low_range}-€{high_range}'
        except Exception as e:
            errorMessage = "Error processing input: {}".format(e)
            return errorMessage

    return app
