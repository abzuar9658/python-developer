from .coffee import Coffee
from db.espresso import espresso

class Espresso(Coffee):
    def set_client(self):
        self.client = espresso
        