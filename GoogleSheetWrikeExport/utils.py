import json
import csv
from pathlib import Path
import pandas as pd


points = {'IEACTPDZJUAA7YIS': 'Acutal points', 'IEACTPDZJUABEXK3': 'Budget points',"IEACTPDZJUABKDUX":"Resourse Type"}
    
def write_to_json(data, path):
    # write data to a json file
    with open(path, 'w') as outfile:
        json.dump(data, outfile)
    return "done"


def json_to_csv(json_path,csv_path):
    df = pd.read_json(json_path)
    df.to_csv(csv_path, index=False)
    
def csv_to_list(path: Path):
    with open(path, encoding='utf-8') as f:
        reader = csv.reader(f)
        return list(reader)
        
        
        # return [row for row in csv.reader(f)]