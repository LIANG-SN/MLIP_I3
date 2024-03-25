import papermill as pm

def retrain_model(n_data):
    pm.execute_notebook(
        'train.ipynb',
        'train_output.ipynb',
        parameters=dict(n_data = n_data)
    )

retrain_model(5000)