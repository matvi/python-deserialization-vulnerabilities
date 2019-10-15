import json

filename = 'json-serialized.untrusted'

with open(filename, 'rb') as file_object:
    raw_data = file_object.read()
    deserialized_data = json.loads(raw_data)
