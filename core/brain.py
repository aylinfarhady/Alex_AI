from core.memory import Memory
from core.personality import Personality

print("BRAIN FILE LOADED")


class Brain:

    def __init__(self):
        self.memory = Memory()
        self.personality = Personality()
        self.name = "Alex"


    def answer(self, text):

        text = text.lower()


        if "hello" in text:
            return "Hello, I am Alex."


        if "who are you" in text:
            return self.personality.describe()


        if "memory" in text:
            return "My memory system is active."


        if "my name is" in text:

            name = text.replace("my name is", "").strip()

            self.memory.save(
                "user_name",
                name
            )

            return "Nice to meet you " + name


        if "what is my name" in text:

            name = self.memory.get("user_name")

            if name:
                return "Your name is " + name

            return "I don't know your name yet."


        return "I am thinking about: " + text