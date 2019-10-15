import pickle

filename = 'serialized.untrusted'

with open(filename, 'rb') as file_object:
    raw_data = file_object.read()
    deserialized_data = pickle.loads(raw_data)
