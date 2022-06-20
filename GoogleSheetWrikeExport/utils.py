import json

def write_to_json(data, path):
    # write data to a json file
    with open(path, 'w') as outfile:
        json.dump(data, outfile)
    return "done"

def read_in_json(path):
    # read in a json file to a dictionary
    with open(path) as json_file:
        data = json.load(json_file)
    return data
