import random
111

class Product:
    """Class attributes"""

    def __init__(self, name=None, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """Determines if the Product will be stolen
        based on price divided by weight."""

        price_oz = self.price / self.weight
        if price_oz < 0.5:
            return "Not so stealable..."
        elif 1 > price_oz >= 0.5:
            return "kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """Determins a Product's chance to combust based on
        flammability times weight."""

        combust = self.flammability * self.weight
        if combust < 10:
            return "...fizzle"
        elif 50 > combust >= 10:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """Child class called BoxingGloves that inherits methods from Product."""

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove"

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif 15 > self.weight >= 5:
            return "Hey that hurt!"
        else:
            return "OUCH!!"
