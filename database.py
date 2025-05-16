import csv
import os
from backend.models.trainer import extract_features

def save_behavior_data(username, behavior_data):
    features = extract_features(behavior_data)
    file_path = f"data/{username}_data.csv"
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["mean_duration", "std_duration", "label"])
        writer.writerow([features[0], features[1], 1])  # 1 = genuine
