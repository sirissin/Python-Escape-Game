
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

