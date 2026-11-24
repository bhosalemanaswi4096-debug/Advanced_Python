import csv
import json

with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)

    data = []

    for row in reader:
        data.append(row)

with open("data.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent=4)

print("CSV converted to JSON successfully!")