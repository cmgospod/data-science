from flask import Flask, render_template, request


def create_app():
    """Create and configure a basic Flask app"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('base.html')

    @app.route('/input', methods=['POST'])
    def retrieval():
        neighbourhood_group = request.values['neighbourhood_group']
        neighbourhood = request.values['neighbourhood']
        latitude = request.values['latitude']
        longitude = request.values['longitude']
        room_type = request.values['room_type']
        minimum_nights = request.values['minimum_nights']
        calculated_host_listings_count = request.values['calculated_host_listings_count']
        availability_365 = request.values['availability_365']
        bathrooms = request.values['bathrooms']
        bedrooms = request.values['bedrooms']
        output = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}" \
            .format(neighbourhood_group, neighbourhood, latitude, \
                longitude, room_type, minimum_nights, calculated_host_listings_count, \
                    availability_365, bathrooms, bedrooms)
        return output
    
    return app