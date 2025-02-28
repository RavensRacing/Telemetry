import csv
import requests
import json
import pandas as pd


with open("sample_lap - 1.csv") as file:
    data = pd.read_csv(file)

    data = data.apply(pd.to_numeric, errors='ignore')

    all_data = data.to_dict(orient='records')
    #print(json.dumps(all_data[0], indent=4))

    values = []
    for record in all_data:
        
        response = requests.post("http://127.0.0.1:8000/telemetry/", json=record, headers={"Content-Type" : "application/json"})
