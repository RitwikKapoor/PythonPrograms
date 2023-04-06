import json

with open('info.json', 'r') as file:
    data = json.load(file)

# data where age >= 30 
filtered_data = [d for d in data if d['age'] >= 30]

with open('filtered_info.json', 'w') as fi:
    json.dump(filtered_data, fi, indent=4)
