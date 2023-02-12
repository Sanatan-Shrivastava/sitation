from flask import Flask, request, jsonify
from Analytics import predictionModel
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/landData", methods=["POST"])
def post_data():
    data = request.get_json()
    # process the data here
    print(data)
    city = data['city']
    sector = data['sector']
    budget = data['budget']
    df_dict = predictionModel(city, sector, budget).to_dict()
    json_string = json.dumps(df_dict)
    return json_string

def sendLandData():
    print(request.form)
    city = request.form['city']
    sector = request.form['sector']
    budget = request.form['budget']
    df_dict = predictionModel(city, sector, budget).to_dict()
    return json.dumps(df_dict)

if __name__ == "__main__":
    app.run(debug=True)
