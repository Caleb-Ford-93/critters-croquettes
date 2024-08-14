from datetime import date


class Frog:
    def __init__(self, name, species):
        self.slithering = True  # ish
        self.name = name
        self.species = species
        self.date_added = date.today
