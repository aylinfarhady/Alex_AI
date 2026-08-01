import json
import os


class Memory:

    def __init__(self):

        self.file = "memory.json"

        if not os.path.exists(self.file):
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump({}, f)


    def load(self):

        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)


    def save(self, key, value):

        data = self.load()

        data[key] = value

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )


    def add_to_list(self, key, value):

        data = self.load()

        if key not in data:
            data[key] = []

        data[key].append(value)

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )


    def get(self, key):

        data = self.load()

        return data.get(key, None)