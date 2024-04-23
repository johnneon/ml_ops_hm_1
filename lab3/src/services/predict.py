import pickle

import pandas as pd


def predict(data):
    """ Predict the class of a given iris sample """

    # Load model
    with open('./model.pkl', 'rb') as file:
        model, scaler = pickle.load(file)
        df = pd.DataFrame(data=data, columns=scaler.feature_names_in_)
        # Prepare data
        scaled_data = scaler.transform(df)
        # Predict
        result = model.predict(scaled_data)[0]
        # Format response
        class_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
        result = class_names[result]

        return {"result": result}
