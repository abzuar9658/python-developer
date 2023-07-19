from .coffee_creator import CoffeeCreator
from coffees.espresso import Espresso

class EspressoCreator(CoffeeCreator):
    def __init__(self):
        self.coffee = Espresso()
        super().__init__()

    def coffee(self):
        return self.coffee

