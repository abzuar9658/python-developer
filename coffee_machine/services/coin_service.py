
class CoinService:
    def __init__(self):
        self.coins = Coins()

    def process_coins(self):
        self.coins.input_coins()