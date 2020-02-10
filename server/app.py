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
@app.route('/firstQuestionData', methods=['GET', 'POST'])
def DeathData():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        state = post_data['state']
        orientation = post_data['orientation']
        question_one_data = data.question_one_data(state, orientation)
        return jsonify(question_one_data)

#This route will get the data for the map page
@app.route('/fetchMapData', methods=['GET', 'POST'])
def map_data():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        map_data = data.get_map_data(post_data)
        return jsonify(map_data)

if __name__ == '__main__':
    app.run()
