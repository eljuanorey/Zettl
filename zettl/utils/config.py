from zettl import *

def get_config_parameter(json_path, parameter_key):
    with open(json_path, 'r') as f:
        config = json.load(f)
    return config.get(parameter_key, None)

def edit_config_parameter(json_path, param_name, new_value):
    with open(json_path, 'r') as file:
        data = json.load(file)
    data[param_name] = new_value
    with open(json_path, 'w') as file:
        json.dump(data, file, indent=4)