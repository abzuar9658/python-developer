from .coffee import Coffee
from db.latte import latte
import pdb

class Latte(Coffee):
    def get_ingredients(self):
        if not self.ingredients:
            self.ingredients['water'] = latte['water']
            self.ingredients['milk'] = latte['milk']
            self.ingredients['coffee'] = latte['coffee']

        return self.ingredients

    def get_price(self):
        if not self.price:
            self.price = latte['price']
        return self.price
        