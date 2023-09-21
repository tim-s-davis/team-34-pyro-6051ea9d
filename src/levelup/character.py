class Character:
    name = ""

    def __init__(self, character_name):
        if character_name == "":
            self.name = 'Character'
        else:
            self.name = character_name
