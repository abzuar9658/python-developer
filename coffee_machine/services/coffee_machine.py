class CoffeeMachine:
    def __init__(self, coffee_creator):
        self.coffee_creator = coffee_creator
        self.coins_service = Coins()

        self.errors = []

    def process(self):
        coffee_creator.verify_sufficient_resources()