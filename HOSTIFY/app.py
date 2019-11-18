from flask import Flask, render_template, request


def create_app():
    """Create and configure a basic Flask app"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('base.html')

    @app.route('/input', methods=['POST'])
    def retrieval():
        result1 = request.values['input1']
        result2 = request.values['input2']
        output = result1 + " " + result2
        return output
    
    return app