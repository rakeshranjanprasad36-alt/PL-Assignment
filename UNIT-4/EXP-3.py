[
    {"name": "Rakesh", "age": 20, "city": "Pune"},
    {"name": "Rahul", "age": 22, "city": "Mumbai"},
    {"name": "Aman", "age": 21, "city": "Delhi"}
]
import json
import csv
json_file = "data.json"
csv_file = "output.csv"

with open(json_file, "r") as file:
    data = json.load(file)   
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    
    
    header = data[0].keys()
    writer.writerow(header)
    

    for item in data:
 writer.writerow(item.values())

print("JSON data successfully converted to CSV.")
 import json
import csv

with open("data.json", "r") as file:
    data = json.load(file)

with open("output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    
    writer.writeheader()
    writer.writerows(data)

print("Conversion completed.")