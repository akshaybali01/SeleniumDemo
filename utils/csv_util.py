import csv
import os

#Read CSV
def read_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"file is missing, {file_path}")
    with open(file_path) as file:
        return list(csv.DictReader(file))