# This file defines the API routes for the application

from flask import Blueprint, request, jsonify
from app.data_loader import load_historical_data

api = Blueprint('api', __name__) # Define a `Blueprint` named `api` to define a collection of routes

@api.route('/load_data', methods=['POST']) # a route `/load_data` is defined to handle POST requests
# it extracts `symbol`, `start_date`, `end_date` from the request JSON and uses `load_historical_data` to fetch the data
# the result is returned as a JSON response
def load_data():
    data = request.json
    symbol = data.get('symbol')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    historical_data = load_historical_data(symbol, start_date, end_date)
    # consider adding timeframe, i.e. minute, hour, day, month, etc.
    return jsonify(historical_data), 200

def init_routes(app):
    app.register_blueprint(api, url_prefix='/api')


