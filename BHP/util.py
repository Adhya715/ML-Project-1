import json
import pickle
import numpy as np

# Global variables to hold the model and data
__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        # Find the index of the location in our columns
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    # Create a numpy array of zeros
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    # If the location is found, set its specific index to 1 (One-Hot Encoding)
    if loc_index >= 0:
        x[loc_index] = 1

    # Return the predicted price rounded to 2 decimal places
    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    # Load the columns JSON file
    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # Locations start from index 3

    global __model
    # Load the binary pickle model
    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ == '__main__':
    load_saved_artifacts()
    # Test call to ensure it works
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
