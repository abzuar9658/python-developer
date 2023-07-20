from .coffee import Coffee
from db.espresso import espresso

class Espresso(Coffee):
    def get_ingredients(self):
        if not self.ingredients:
            self.ingredients['water'] = espresso['water']
            self.ingredients['milk'] = espresso['milk']
            self.ingredients['coffee'] = espresso['coffee']

        return self.ingredients

    def get_price(self):
        if not self.price:
            self.price = espresso['price']
        return self.price
        