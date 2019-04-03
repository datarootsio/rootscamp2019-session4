import hashlib
from functools import lru_cache

from sklearn.externals import joblib
import connexion
import git
import contexttimer as ct


model_file = 'model.joblib'
clf = joblib.load(model_file)

@lru_cache()
def get_model_hash():
    # note, adjust for large files (read in chunks)
    with open(model_file, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def get_git_commit():
    repo = git.Repo(search_parent_directories=True)
    return repo.head.object.hexsha

def predict(body):
    with ct.Timer() as t:
        pred = clf.predict(body).tolist()

    resp = {
        'metadata': {
            'git_commit': get_git_commit(),
            'prediction_elapsed_time': t.elapsed,
            'model_sha256': get_model_hash()
        },
        'prediction': pred
    }

    return resp


app = connexion.App('Super Duper Fancy Pansy API', specification_dir='./openapi/')
app.add_api('super_duper_fancypansy_api.yaml')
app.run(port=8080, debug=True)
