
from coins.coin import Coin

class CoinService:
    def __init__(self):
        self.coin = Coin()
        self.collected_coints = 0

    def collect_coins(self):
        total = 0

        while True:
            for coin in self.coin.coin_types.keys():
                count = int(input(f"How many {coin}s you want to insert? (0 if nothing): "))
                total += count * self.coin.coin_types[coin]
        
            self.collected_coints = round(total, 2)

            print(f"You have {self.collected_coints} in balance")

            exit = input("0 to exit coins input: ")
            if exit == '0':
                break
    
    def get_collected_coints(self):
        return self.collected_coints