"""
Alex AI Memory System
"""

import json
import os
import Config


class MemoryManager:

    def init(self):

        self.file = Config.MEMORY_FILE
        self.create_memory()


    def create_memory(self):

        folder = os.path.dirname(self.file)

        if not os.path.exists(folder):
            os.makedirs(folder)

        if not os.path.exists(self.file):

            with open(
                self.file,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    [],
                    f,
                    indent=4
                )


    def load_memory(self):

        try:

            with open(
                self.file,
                "r",
                encoding="utf-8"
            ) as f:

                return json.load(f)

        except:

            return []


    def save_message(self, sender, message):

        memory = self.load_memory()

        memory.append(
            {
                "sender": sender,
                "message": message
            }
        )

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                memory,
                f,
                indent=4,
                ensure_ascii=False
            )


    def get_last_messages(self, amount=5):

        memory = self.load_memory()

        return memory[-amount:]


    def clear_memory(self):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                [],
                f,
                indent=4
            )