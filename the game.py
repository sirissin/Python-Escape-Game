
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

    # defining what is in the room
    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    # making sure that the code is set
    def check_code(self, code):
        return self.escape_code == code

    # List of game objects
    def get_game_object_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names


# Establishing the Game class
class Game:
    def __init__(self):
        self.attempts = 0
        objects = self.create_objects()
        self.room = Room(5412, objects)

    # The objects used to solve the riddle
    def create_objects(self):
        return [
            GameObject("Sweater", "It is a partially shredded red sweater and the tag says it is size "
                                  "12.", "It is fuzzy, and feels like it is brand new.", "It faintly smells"
                                    "of lavender."),
            GameObject("Chair", "It is a three-legged chair.", "Upon feeling the chair over, you "
                                "notice that a leg had been snapped off.", "It smells of old wood."),
            GameObject("Journal", "The only entry states that the time should only be read in hours, "
                                  "then minutes, then seconds (H-M-S).", "It feels old and heavily worn.", "It"
                                    "smells musty."),
            GameObject("Bowl of Soup", "It appears to be mushroom soup.", "It is cold.", "It "
                                 "has the aroma of 5 different types of spices."),
            GameObject("Clock", "The hour hand is pointing towards the soup, the minute hand towards the"
                                "chair, and the second hand towards the sweater.", "The clock feels light, as if "
                                   "missing components.", "It smells like plastic and metal.")
        ]

    # Runs the prompt, ergo defines a turns
    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = input(prompt)

    # The text prompt that allows the user to choose what to do
    def get_room_prompt(self):
        prompt = "Enter the 4 digit lock code or choose an item to interact with:\n"
        names = self.room.get_game_object_names()
        index = 1
        for name in names:
            prompt += f"{index}. {name}\n"
            index += 1
        return prompt


game = Game()
game.take_turn()
