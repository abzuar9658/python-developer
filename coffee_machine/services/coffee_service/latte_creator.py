from .coffee_creator import CoffeeCreator
from coffees.latte import Latte

class LatteCreator(CoffeeCreator):
    def __init__(self):
        self.coffee = Latte()
        super().__init__()

    def coffee(self):
        return self.coffee

