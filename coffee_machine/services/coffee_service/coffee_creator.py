from abc import ABC, abstractmethod
from db.resources import resources
import pdb
from coffees.latte import Latte

class CoffeeCreator(ABC):
    @abstractmethod
    def coffee(self):
        pass

    def verify_sufficient_resources(self):
        errors = []

        coffee_ingredients = self.coffee.get_ingredients()
        for ingredient in coffee_ingredients.keys():
            if(resources[ingredient] < coffee_ingredients[ingredient]):
                errors.append(f"Sorry there is not enough {ingredient}")

        if errors:
            raise Exception(errors)

    def coffee_price(self):
        return self.coffee.get_price()

    def make_coffee(self):
        coffee_ingredients = self.coffee.get_ingredients()
        for ingredient in coffee_ingredients.keys():
            resources[ingredient] = resources[ingredient] - coffee_ingredients[ingredient]
        
        print(f"Here is your cofee. Enjoy!")
        