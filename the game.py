
# Objects class
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


# The Room class
class Room:

    escape_code = 0
    game_objects = []

    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    def check_code(self, code):
        return self.escape_code == code

    def get_game_object_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names


game_object = GameObject("Knife", "Some appearance", "Some feel", "Some Smell")

game_object.name = "Spoon"
print(game_object.sniff())
