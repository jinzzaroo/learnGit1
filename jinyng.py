class Jinyng:

    def __init__(age, company, school):
        self.age = age
        self.school = school
        self.company = company

    def print():
        print(f"Hi, I'm jinyng.\n I'm {self.age}"+
              f"I graduated from {self.school}.\n"+
              f"I work for {self.company}")

    def chat(conversation):
        return "I don't know that"

    def sayHi(name):
        return f"Hi,{name}! I am jinyng"

if __name__ == "__main__":

    jinyng=Jinyng(25, "ChungBuk Univ.", "asd")

    jinyng.print()
