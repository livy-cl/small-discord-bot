def read_json(file_name: str):
    try:
        with open(file_name) as file:
            from json import load
            data = load(file)
        return data
    except FileNotFoundError:
        print("Failed reading the json file " + file_name)


def write_json(file_name: str, data) -> bool:
    try:
        with open(file_name, 'w') as file:
            from json import dump
            dump(data, file)
            return True
    except FileNotFoundError:
        print("Failed reading the json file " + file_name)
        return False
