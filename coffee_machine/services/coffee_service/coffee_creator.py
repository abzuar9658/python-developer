from abc import ABC, abstractmethod
from db.resources import resources
import pdb
from coins.coins import Coins
from coffees.latte import Latte

class CoffeeCreator(ABC):
    @abstractmethod
    def coffee(self):
        pass

    def verify_sufficient_resources(self):
        errors = []
        ingredients = self.coffee.get_ingredients()
        for ingredient in ingredients.keys():
            if(resources[ingredient] < ingredients[ingredient]):
                errors.append(f"Sorry there is not enough {ingredient}")

        raise Exception(errors) if errors else None