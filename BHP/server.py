from flask import Flask, request, jsonify
import util # Import the helper script we just wrote

app = Flask(__name__) # Create the Flask app

# Route to get all location names for our dropdown
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*') # Fix for browser security
    return response

# Route to predict the price based on user input
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    # Get values from the form request
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # Get prediction from util.py
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts() # Load the model into memory first
    app.run() # Run on port 5000
