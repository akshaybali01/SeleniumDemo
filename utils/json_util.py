import json
import os
from pathlib import Path

def read_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"file is missing, {file_path}")
    with open(file_path) as file:
        return json.load(file)

file_path = Path(__file__).parent.parent / "data/login_data.json"
#print(read_json(file_path))
data = []
for item in read_json(file_path):
    #print(item)
    if item["login_type"]=="valid":
        data.append(item)
print(data)
