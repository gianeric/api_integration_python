import json

def load_payload(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
