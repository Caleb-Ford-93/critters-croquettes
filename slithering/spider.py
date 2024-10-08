from datetime import date


class Spider:
    def __init__(self, name, species, food):
        self.slithering = True  # ish
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"
