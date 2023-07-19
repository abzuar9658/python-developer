from db.resources import resources

class Coins:
    def __init__(self):
        self.total_coins = 0
        self.coins = {
        'quarter': 0.25,
        'diner': 0.10,
        'nickle': 0.05,
        'pennie': 0.01
        }

    def get_total_coins(self):
        return self.total_coins

    def input_coins(self):
        total = 0

        while True:
            for coin in self.coins.keys():
                count = int(input(f"How many {coin}s you want to insert? (0 if nothing): "))
                total += count * self.coins[coin]
        
            self.total_coins = round(total, 2)

            print(f"You have {self.total_coins} in balance")

            exit = input("0 to exit coins input")
            if exit == '0':
                break