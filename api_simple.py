"""Simple API implementation."""


from sklearn.externals import joblib
from flask import Flask, request, jsonify

app = Flask('Super Duper API')
clf = joblib.load('model.joblib')


@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict train delays.

    :return: prediction
    """
    body = request.get_json()
    pred = clf.predict(body).tolist()

    return jsonify(pred)


app.run(debug=True, port=8080)
