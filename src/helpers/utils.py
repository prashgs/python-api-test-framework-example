import toml
import json


def read_data_file(filename: str, type: str) -> dict:
    data = None

    match type:
        case 'toml':
            with open(filename, 'r') as f:
                data = f.read()
                data = toml.loads(data)
        case 'json':
            with open(filename, 'r') as f:
                data = json.load(f)
    return data
