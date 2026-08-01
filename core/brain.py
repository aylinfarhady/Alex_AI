from core.memory import Memory
from core.personality import Personality
from core.language import LanguageEngine


class Brain:

    def __init__(self):
        self.memory = Memory()
        self.personality = Personality()
        self.language = LanguageEngine()
        self.name = "Alex"


    def answer(self, text):

        text = text.lower()

        analysis = self.language.analyze(text)


        if analysis["type"] == "like":

            self.memory.add_to_list(
                "likes",
                analysis["value"]
            )

            return "I will remember that you like " + analysis["value"]


        if "hello" in text or "hi" in text:

            return "Hello, I am Alex."


        if "who are you" in text:

            return self.personality.describe()


        if "memory" in text:

            return "My memory system is active."


        if "my name is" in text:

            name = text.replace("my name is", "").strip()

            self.memory.save(
                "name",
                name
            )

            return "Nice to meet you " + name


        if "what is my name" in text:

            name = self.memory.get("name")

            if name:

                return "Your name is " + name

            return "I don't know your name yet."


        return "I am thinking about: " + text