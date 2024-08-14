from datetime import date


class Llama:
    def __init__(self, name, species):
        self.walking = True
        self.name = name
        self.species = species
        self.date_added = date.today()
