import json
import os


class Memory:

    def __init__(self):

        self.file = "memory.json"

        if not os.path.exists(self.file):
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump({}, f)


    def save(self, key, value):

        with open(self.file, "r", encoding="utf-8") as f:
            data = json.load(f)

        data[key] = value

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)



    def get(self, key):

        with open(self.file, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data.get(key, None)