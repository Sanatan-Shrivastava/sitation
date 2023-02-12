from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/landData',methods=["POST"])
def sendLandData():
    city = request.form['city']
    sector = request.form['sector']
    return {'city':city,'sector':sector}


if __name__ == '__main__':
    app.run(debug=True)
