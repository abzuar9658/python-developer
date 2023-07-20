from .coffee import Coffee
from db.latte import latte
import pdb

class Latte(Coffee):        
    def set_client(self):
        self.client = latte