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
],
"site":[
    "AT&T Stadium|| 1 AT&T Way, Arlington, TX 76011",
"American Airlines Center|| 2500 Victory Ave, Dallas, TX 75219",
"Dallas World Aquarium|| 1801 N Griffin St, Dallas, TX 75202",
"Klyde Warren Park|| 2012 Woodall Rodgers Fwy, Dallas, TX 75201",
"Dallas Arboretum and Botanical Garden|| 8525 Garland Rd, Dallas, TX 75218",
"Perot Museum of Nature and Science|| 2201 N Field St, Dallas, TX 75201",
"Bishop Arts District|| Bishop Ave, Dallas, TX 75208",
"Museum at Dealey Plaza|| 411 Elm St, Dallas, TX 75202",
"Reunion || 300 Reunion Blvd E, Dallas, TX 75207"
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
"64757"],
 "site":[
    "Universal Studios Hollywood|| 100 Universal City Plaza, Universal City, CA 91608",
"Dolby Theatre|| 6801 Hollywood Blvd, Hollywood, CA 90028",
"Getty Center|| 1200 Getty Center Dr, Los Angeles, CA 90049",
"Sunset Strip|| 9039 Sunset Blvd, West Hollywood, CA 90069",
"Walk of Fame|| Hollywood Blvd, Los Angeles, CA 90028",
"The Grove|| 189 The Grove Dr, Los Angeles, CA 90036",
"LACMA (Los Angeles County Museum of Art)|| 5905 Wilshire Blvd, Los Angeles, CA 90036",
"The Broad|| 221 S Grand Ave, Los Angeles, CA 90012",
"Venice Beach Boardwalk|| 1800 Ocean Front Walk, Venice, CA 90291",
"The Hollywood Sign|| Griffith Park, Los Angeles, CA 90027"
 ]
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
],
"site":[
    "The Magic Garden|| 1020 South St, Philadelphia, PA 19147",
"Edgar Allan Poe National Historic Site|| 532 N 7th St, Philadelphia, PA 19123",
"Reading Terminal Market|| 1136 Arch St, Philadelphia, PA 19107",
"Bartram Garden|| 5400 Lindbergh Blvd, Philadelphia, PA 19143",
"Schuylkill River Trail|| Schuylkill River Trail, Philadelphia, PA 19130",
"Mount Moriah Cemetery|| 6201 Kingsessing Ave, Philadelphia, PA 19142"
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
    for data in sorted_df[:5]:
        elem = {}
        elem['city'] = data['County Name']
        elem['sector'] = sector
        elem['budget'] = budget
        elem['roi'] = data['Revenue']
        elem['qoz'] = qoz[random.randint(0,2)]
        elem['landval'] = dum[city]['landval'][random.randint(0,5)]
        elem['landarea'] = dum[city]['landarea'][random.randint(0,5)]
        elem['addr'] = dum[city]['addr'][random.randint(0,5)]
        result.append(elem) 
    return result

