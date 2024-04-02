import pickle
import numpy as np

## Load the model
reg_model = pickle.load(open("regmodel.pkl", "rb"))
scalar = pickle.load(open("scaling.pkl", "rb"))


def predict(data):
    new_data = scalar.transform(np.array(data).reshape(1, -1))
    output = reg_model.predict(new_data)
    return output[0]
