from abc import ABC, abstractmethod

class Coffee(ABC):
    def __init__(self):
        self.ingredients = {}
        self.set_client()

    def get_ingredients(self):
        if not self.ingredients:
            self.ingredients['water'] = self.client['water']
            self.ingredients['milk'] = self.client['milk']
            self.ingredients['coffee'] = self.client['coffee']

        return self.ingredients

    def get_price(self):
        return self.client['price']
    
    def get_name(self):
        return self.client['name']

    @abstractmethod
    def set_client(self):
        pass