from datetime import date


class Spider:
    def __init__(self, name, species):
        self.slithering = True  # ish
        self.name = name
        self.species = species
        self.date_added = date.today
