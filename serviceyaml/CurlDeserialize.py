import yaml

filename = 'curl-serialized.untrusted'

with open(filename, 'r') as file_object:
    raw_data = file_object.read()
    deserialized_data = yaml.load(raw_data)
