class Personality:

    def __init__(self):

        self.name = "Alex"

        self.traits = {
            "friendly": 100,
            "curious": 100,
            "logic": 95
        }


    def describe(self):

        return (
            "I am Alex. "
            "I am friendly, curious and logical."
        )