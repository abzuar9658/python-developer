from .coffee import Coffee
from db.cuppicino import cuppicino

class Cuppicino(Coffee):
    def set_client(self):
        self.client = cuppicino