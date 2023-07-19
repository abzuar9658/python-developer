from services.coffee_service.cuppicino_creator import CuppicinoCreator
from services.coffee_service.espresso_creator import EspressoCreator
from services.coffee_service.latte_creator import LatteCreator

def start():
    coffee = str(input("What would you like? (espresso/latte/cuppicino): "))
    coffee_creator = None

    if coffee == 'cuppicino':
        coffee_creator = CuppicinoCreator()

    elif coffee == 'espresso':
        coffee_creator = EspressoCreator()

    elif coffee == 'latte':
        coffee_creator = LatteCreator()

    else:
        print("Chooese correct options please")

    if coffee_creator:
        coffee_creator.create_coffee()

try:
    start()
except Exception as e:
    print(e)


