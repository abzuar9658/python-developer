from .coffee import Coffee
from db.cuppicino import cuppicino

class Cuppicino(Coffee):
    def get_ingredients(self):
        if not self.ingredients:
            self.ingredients['water'] = cuppicino['water']
            self.ingredients['milk'] = cuppicino['milk']
            self.ingredients['coffee'] = cuppicino['coffee']

        return self.ingredients

    def get_price(self):
        if not self.price:
            self.price = cuppicino['price']
        return self.price
        