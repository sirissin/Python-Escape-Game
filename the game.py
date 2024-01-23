
class GameObject:
    # Properties that belong to the class (not necessary to have since they are also in the function below)
    name = ""
    appearance = ""
    feel = ""
    smell = ""

    # Functions that allow you to take a value for each property
    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    # Different actions you can take
    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"


    def touch(self):
        return f"You touch at the {self.name}. {self.feel}\n"


    def sniff(self):
        return f"You sniff at the {self.name}. {self.smell}\n"


game_object = GameObject("Knife", "Some appearance", "Some feel", "Some Smell")

game_object.name = "Spoon"
print(game_object.sniff())
