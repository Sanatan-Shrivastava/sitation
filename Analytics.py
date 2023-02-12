import pandas as pd
import pickle
import numpy as np
from sklearn import preprocessing


def load_and_predict(filename, input_data):
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    
    # Create an instance of the LabelEncoder class
    encoder = preprocessing.LabelEncoder()

    # Fit the encoder to the categorical values
    encoder.fit(input_data)

    # Encode the categorical values
    encoded_values = encoder.transform(input_data)

    # Reshape the encoded values to be suitable for prediction
    encoded_values = encoded_values.reshape(1, -1)

    # Predict the target using the pre-trained neural network model
    prediction = model.predict(encoded_values)

    # Print the prediction
    print("Prediction:", prediction)
    return prediction

def predictionModel(city, sector, budget):
    pedictedValue = load_and_predict("model.pkl", [city, sector, budget]) 
    #print(pedictedValue[0][0])
    df = pd.read_excel("2019.xlsx")
    filtered_df = df[df['County Name'] == city]
    filtered_df = filtered_df[filtered_df["NAICS Description"].str.contains(
        sector)]
    filtered_df = filtered_df[filtered_df['Revenue'] >= pedictedValue[0][0]]
    sorted_df = filtered_df.sort_values('Revenue', ascending=False)
    sorted_df = sorted_df.drop_duplicates()
    return sorted_df[:5]

