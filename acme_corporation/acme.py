class Product():
    """ Classifies products for Acme Corporation."""
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        """Defines attributes of a product."""
        from random import randint
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """Estimates chance of theft as a function of weight and price"""
        steal = self.price / self.weight
        if steal < 0.5:
            return "Not so stealable..."
        elif steal < 1:
            return "Kinda stealable"
        else:
            return "Very stealable!"

    def explode(self):
        """Estimates explosion risk (coyote not included)."""
        explosion = self.flammability * self.weight
        if explosion < 10:
            return "...fizzle"
        elif explosion < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """Classifies boxing gloves as a subclass of products"""
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
