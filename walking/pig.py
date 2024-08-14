from datetime import date


class Pig:
    def __init__(self, name, species, shift):
        self.walking = True
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
