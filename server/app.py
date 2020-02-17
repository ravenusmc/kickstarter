from flask import Flask, jsonify, request
from flask_cors import CORS

#importing code that I wrote
from data import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

#This route will get the data for the charts
@app.route('/routeOne', methods=['GET', 'POST'])
def routeOne():
    if request.method == 'POST':
        return jsonify(question_one_data)


if __name__ == '__main__':
    app.run()
