from flask import Flask, render_template, request
from joblib import load
import pandas as pd

pipeline = load('MODEL/model.joblib')


def create_app():
    """Create and configure a basic Flask app"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('base.html')

    @app.route('/input', methods=['POST'])
    def retrieval():
        neighbourhood_group = request.values['neighborhood_group']
        neighbourhood = request.values['neighborhood']
        room_type = int(request.values['room_type'])
        minimum_nights = int(request.values['minimum_nights'])
        calculated_host_listings_count = int(request.values['calculated_host_listings_count'])
        availability_365 = int(request.values['availability_of_year'])
        bathrooms = int(request.values['bathroom_number'])
        bedrooms = int(request.values['bedroom_number'])

        predict_thing = pd.DataFrame(columns=['neighbourhood_group', 'neighbourhood', 'room_type', 'minimum_nights',
       'calculated_host_listings_count', 'availability_365', 'bathrooms',
       'bedrooms'], data=[[1,1,room_type,minimum_nights,calculated_host_listings_count,availability_365,bathrooms,bedrooms]])

        prediction = pipeline.predict(predict_thing)[0].round(2)

        #output = "{}, {}, {}, {}, {}, {}, {}, {}" \
        #    .format(neighbourhood_group, neighbourhood, \
        #           room_type, minimum_nights, calculated_host_listings_count, \
        #           availability_365, bathrooms, bedrooms)
        return str(prediction)
    
    return app