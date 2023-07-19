from abc import ABC, abstractmethod

class Coffee(ABC):
    def __init__(self):
        self.ingredients = {}
        self.price = None

    @abstractmethod
    def get_ingredients(self):
        pass

    @abstractmethod
    def get_price(self, param):
        pass