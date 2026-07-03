import pickle
import numpy as np

# -----------------------------
# Load Trained Model
# -----------------------------

model = pickle.load(open("models/model.pkl", "rb"))


# -----------------------------
# Prediction Function
# -----------------------------

def predict_crop(N, P, K,
                 temperature,
                 humidity,
                 ph,
                 rainfall):

    features = np.array([[
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    ]])

    prediction = model.predict(features)

    return prediction[0]