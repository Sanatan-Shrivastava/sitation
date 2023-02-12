import pandas as pd
import pickle
import numpy as np

def load_and_predict(filename, input_data):
    with open(filename, 'rb') as file:
        model = pickle.load(file)

    # Ensure input data is in the correct format
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction

def predictionModel( city, sector, budget):
    pedictedValue = load_and_predict("model.pkl", [city, sector, budget]) 
    df = pd.read_excel("yearlyData/2019.xlsx")
    filtered_df = df[df['County Name'] == city]
    filtered_df = df[sector in df['NAICS Description']]
    filtered_df = df[df['Revenue'] >= pedictedValue]
    return filtered_df

print(predictionModel("Dallas", "education","12000"))