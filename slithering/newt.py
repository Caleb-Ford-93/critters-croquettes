from datetime import date


class Newt:
    def __init__(self, name, species):
        self.slithering = True
        self.name = name
        self.species = species
        self.date_added = date.today()
