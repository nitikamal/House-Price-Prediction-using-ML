import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None




def load_saved_files():
    print("loading saved files....start")
    global __data_columns
    global __locations
    global __model

    with open("./exported_files/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    with open("./exported_files/bangaluru_home_prices.pickle","rb") as f:
        __model = pickle.load(f)
    print("loading saved files.....done")    

def get_location_names():
    return __locations

def get_estimated_price(location, sqft, BHK, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = BHK
    
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)
if __name__ == "__main__":
    load_saved_files()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 2))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalkhali', 1000, 2, 2))
    


        