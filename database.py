import json


class DataBase:
    def __init__(self, filename: str):
        self.filename = filename

    def set_data(self, key, value):
        data = {}

        with open(self.filename, "r") as f:
            data = json.loads(f.read())

        data[key] = value

        with open(self.filename, "w") as f:
            f.write(json.dumps(data, indent=4))

    def get_data(self, key):
        with open(self.filename, "r") as f:
            return json.loads(f.read()).get(key)
