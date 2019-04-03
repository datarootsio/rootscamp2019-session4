from sklearn.externals import joblib
import connexion
import git
import contexttimer as ct

clf = joblib.load('model.joblib')


def get_git_commit():
    repo = git.Repo(search_parent_directories=True)
    return repo.head.object.hexsha

def predict(body):
    with ct.Timer() as elapsed_time:
        pred = clf.predict(body).tolist()

    resp = {
        'metadata': {
            'git_commit': get_git_commit(),
            'timing': elapsed_time
        },
        'prediction': pred
    }

    return resp


app = connexion.App('Super Duper Fancy Pansy API', specification_dir='./openapi/')
app.add_api('super_duper_fancypansy_api.yaml')
app.run(port=8080, debug=True)
