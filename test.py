import json

file_name=open("New_data/data.json")

data = json.load(file_name)
f=[]
def send_data():
    for keys in data.keys():
        f.append(data[keys][1]["act_info"])
    return f

