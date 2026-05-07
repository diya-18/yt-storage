# to store original file size, frame size, filename and number of frames.
import json
import os

def save_metadata(path, metadata):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(metadata, f, indent=4)

def load_metadata(path):
    with open(path, "r") as f:
        return json.load(f)