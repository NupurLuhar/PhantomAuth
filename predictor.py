import joblib
import numpy as np
from backend.models.trainer import extract_features

def authenticate_user(username, behavior_data):
    model = joblib.load(f"data/{username}_model.pkl")
    features = extract_features(behavior_data)
    prob = model.predict_proba([features])[0][1]
    return prob > 0.7
