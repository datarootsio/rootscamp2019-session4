"""Connexxion API example."""

from sklearn.externals import joblib
import connexion

clf = joblib.load('model.joblib')


def predict(body):
    """
    Predict train delays.

    :param body: the request body
    :return: prediction response object
    """
    return clf.predict(body).tolist()


app = connexion.App('Super Duper API', specification_dir='./openapi/')
app.add_api('super_duper_api.yaml')
app.run(port=8080, debug=True)
g