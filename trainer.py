import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

def extract_features(data):
    df = pd.DataFrame(data)
    keystroke_times = []

    down_times = {}
    for i, row in df.iterrows():
        if row["type"] == "keydown":
            down_times[row["key"]] = row["timestamp"]
        elif row["type"] == "keyup" and row["key"] in down_times:
            duration = row["timestamp"] - down_times[row["key"]]
            keystroke_times.append(duration)

    return [np.mean(keystroke_times), np.std(keystroke_times)]

def train_user_model(username):
    df = pd.read_csv(f"data/{username}_data.csv")
    X = df[["mean_duration", "std_duration"]]
    y = df["label"]
    clf = RandomForestClassifier()
    clf.fit(X, y)
    joblib.dump(clf, f"data/{username}_model.pkl")
