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
        data = Data()
        post_data = request.get_json()
        category = post_data['category']
        state = post_data['state']
        currency = post_data['currency']
        country = post_data['country']
        start_date = post_data['startDate']
        end_date = post_data['endDate']
        money_goal = float(post_data['moneyGoal'])
        backers = float(post_data['backers'])
        first_chart_data = data.first_chart(category, state, currency, country, start_date, end_date, money_goal, backers)
        return jsonify(first_chart_data)

#This route will get the data for the successful by category chart
@app.route('/SuccessfulByCategory', methods=['GET', 'POST'])
def Successful_By_Category_Route():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        successful_by_category_data = data.successful_by_category(post_data)
        return jsonify(successful_by_category_data)

#This route will get the data for the failures by category chart
@app.route('/FailuresByCategory', methods=['GET', 'POST'])
def Failures_By_Category_Route():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        failures_by_category_data = data.failures_by_category(post_data)
        return jsonify(failures_by_category_data)

#This route will get the data for the failures and successs chart
@app.route('/SuccessAndFailures', methods=['GET', 'POST'])
def Success_And_Failures_chart():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        failures_by_category_data = data.Success_And_Failures_chart(post_data)
        return jsonify(failures_by_category_data)


if __name__ == '__main__':
    app.run()
