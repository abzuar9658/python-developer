from .coffee_creator import CoffeeCreator
from coffees.cuppicino import Cuppicino

class CuppicinoCreator(CoffeeCreator):
    def __init__(self):
        self.coffee = Cuppicino()
        super().__init__()

    def coffee(self):
        return self.coffee

