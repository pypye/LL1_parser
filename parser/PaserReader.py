import json

def parse(string):
    data = string.split()
    data_obj = []
    current_obj = []
    for x in data:
        if x == "|":
            data_obj.append(current_obj)
            current_obj = []
        else:
            current_obj.append(x)
        
    if len(current_obj) > 0:
        data_obj.append(current_obj)
        
    return data_obj


def parserReader(file):
    with open(file, 'r') as f:
        data = f.read()
        data = json.loads(data)
        for key, value in data.items():
            data[key] = parse(value)
        return data