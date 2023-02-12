from flask import Flask, request
from Analytics import predictionModel

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/landData',methods=["POST"])
def sendLandData():
    city = request.form['city']
    sector = request.form['sector']
    budget = request.form['budget']
    return predictionModel(city, sector, budget) 


if __name__ == '__main__':
    app.run(debug=True)
