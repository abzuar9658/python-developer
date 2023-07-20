from db.resources import resources
from services.coffee_service.cuppicino_creator import CuppicinoCreator
from services.coffee_service.espresso_creator import EspressoCreator
from services.coffee_service.latte_creator import LatteCreator
from .coin_service import CoinService

class CoffeeMachine:
    def __init__(self, coffee):
        self.coffee_creator = self.coffee_creator(coffee)
        self.coin_service = CoinService()

    def process(self):
        self.coffee_creator.verify_sufficient_resources()
        self.coin_service.collect_coins()
        self.verify_enough_coins()
        self.do_transaction()
        self.coffee_creator.make_coffee()


    def verify_enough_coins(self):
        if self.coin_service.get_collected_coints() < self.coffee_creator.coffee_price():
            raise Exception("Sorry that's not enough money. Money refunded.")

    def do_transaction(self):
        resources['money'] = resources['money'] + self.coffee_creator.coffee_price()
        change = self.coin_service.get_collected_coints() - self.coffee_creator.coffee_price()

        if change == 0: return

        print(f"Here is your change worth: ${change}")
         
    def coffee_creator(self, coffee):
        if coffee == 'cuppicino':
            coffee_creator = CuppicinoCreator()

        elif coffee == 'espresso':
            coffee_creator = EspressoCreator()

        elif coffee == 'latte':
            coffee_creator = LatteCreator()

        else:
            raise Exception("Choose correct options please")

        return coffee_creator
            