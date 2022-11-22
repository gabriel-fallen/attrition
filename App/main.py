import os, pickle
import logging
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/api/predict', methods=['POST'])
def predict():
  try:
    # load and parse input
    data = request.json
    vector = [
        data['age'],
        data['travel'],
        data['department'],
        data['distance'],
        data['education'],
        data['gender'],
        data['satisfaction'],
        data['maritalstatus'],
        data['income'],
        data['overtime'],
        data['totalyears'],
        data['years'],
        data['lastpromotion']
    ]
    # app.logging.info(f'vector: {vector}')
    print(f'vector: {vector}\n')

    # load the model
    with open(os.path.join('data', 'logistic.pkcls'), 'rb') as file:
      model = pickle.load(file)

    predictions = model(vector, 1)
    # app.logging.info(f'predictions: {predictions}')
    print(f'predictions: {predictions}\n')

    # send the response
    return jsonify({ "predictions": { "leave": predictions[0], "stay": predictions[1] } })
  except Exception as e:
    return jsonify({"error": repr(e)})

app.logger.setLevel(logging.INFO)
app.run(host='0.0.0.0', port=8080)
