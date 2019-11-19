from flask import Flask, render_template, request


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
        room_type = request.values['room_type']
        minimum_nights = request.values['minimum_nights']
        calculated_host_listings_count = request.values['calculated_host_listings_count']
        availability_365 = request.values['availability_of_year']
        bathrooms = request.values['bathroom_number']
        bedrooms = request.values['bedroom_number']
        output = "{}, {}, {}, {}, {}, {}, {}, {}" \
            .format(neighbourhood_group, neighbourhood, \
                   room_type, minimum_nights, calculated_host_listings_count, \
                   availability_365, bathrooms, bedrooms)
        return output
    
    return app