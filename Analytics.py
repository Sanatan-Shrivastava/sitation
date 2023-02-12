import pandas as pd
import pickle
import numpy as np
import random
from sklearn import preprocessing

dum = {
    "Dallas":{
        "landval":["72700",
"47400",
"55800",
"81180",
"53720",
"45260",
"48720",
"51540",
"35680",
"31520",
"43700",
"36740",
"38740"],
"landarea":[
    "626",
"728",
"745",
"1021",
"1061",
"744",
"724",
"589",
"756",
"669",
"1025",
"621",
"693"
]
    },
    "Los Angeles":{
        "landval":[
             "106006",
             "971461",
             "1073132",
             "574890",
             "586335",
             "1609084",
             "780951",
             "1300272",
        ],
        "landarea":["3540",
"34910",
"8275",
"61535",
"65152",
"104522",
"14390",
"44729",
"25844",
"6267",
"63937",
"64757"]
        },
    "Philadelphia":{
        "landval":[
            "40040",
"49300",
"51040",
"136240",
"103320",
"101200",
"40780",
"40860",
"49700",
"63800",
"48420"],
"landarea":[
    "626",
"728",
"745",
"1021",
"1061",
"744",
"724",
"589",
"756",
"669",
"1025",
"621",
"693"
]
    }
}
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
    qoz=['Yes','No']
    df = pd.read_excel("2019.xlsx")
    filtered_df = df[df['County Name'] == city]
    filtered_df = filtered_df[filtered_df["NAICS Description"].str.contains(
        sector)]
    filtered_df = filtered_df[filtered_df['Revenue'] >= pedictedValue[0][0]]
    sorted_df = filtered_df.sort_values('Revenue', ascending=False)
    sorted_df = sorted_df.drop_duplicates()
    result =[]
    for _,data in sorted_df[:5].iterrows():
        elem = {}
        elem['city'] = data['County Name']
        elem['sector'] = sector
        elem['budget'] = budget
        elem['roi'] = data['Revenue']
        elem['qoz'] = qoz[random.randint(0,1)]
        elem['landval'] = dum[city]['landval'][random.randint(0,5)]
        elem['landarea'] = dum[city]['landarea'][random.randint(0,5)]
        result.append(elem) 
    return result

