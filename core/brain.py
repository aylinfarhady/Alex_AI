print("BRAIN FILE LOADED")
class Brain:

    def __init__(self):
        self.name = "Alex"


    def answer(self, text):

        text = text.lower()

        if "hello" in text:
            return "Hello, I am Alex."

        if "who are you" in text:
            return "I am Alex AI. I am learning and improving."

        if "memory" in text:
            return "My memory system is active."

        return "I am thinking about: " + text