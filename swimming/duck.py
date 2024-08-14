from datetime import date


class Duck:
    def __init__(self, name, species):
        self.swimming = True
        self.name = name
        self.species = species
        self.date_added = date.today
