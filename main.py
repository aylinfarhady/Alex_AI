print("THIS IS NEW MAIN")
from core.brain import Brain


class AlexAI:

    def __init__(self):
        print("CREATING BRAIN")
        self.brain = Brain()
        print("BRAIN READY")


    def run(self):

        print("Alex: Good afternoon, I am online.")
        print("Type exit to close Alex.")

        while True:

            user = input("You: ")

            if user.lower() == "exit":
                print("Alex: Goodbye.")
                break

            response = self.brain.answer(user)

            print("Alex:", response)



if __name__ == "__main__":

    alex = AlexAI()
    alex.run()