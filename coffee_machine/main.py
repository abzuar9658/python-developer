from services.coffee_machine import CoffeeMachine
from services.report_service import ReportService

def start():
    while True:
        choice = int(input("Please choose option 1. Report, 2. Drink Cofee: "))
        if choice == 1:
            ReportService.report()
            print('\n')
        elif choice == 2:
            coffee = str(input("What would you like? (espresso/latte/cuppicino): "))
            CoffeeMachine(coffee).process()

try:
    start()
except Exception as e:
    print(e)


