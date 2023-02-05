ideas = []
def ideabank():
    while True:
        user_idea = input("What is your new idea?: ")
        ideas.append(user_idea)
        for idea in ideas:
            number = ideas.index(idea) + 1
            print(number, ". ", idea, sep = "")
ideabank()
