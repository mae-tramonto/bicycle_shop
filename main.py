from ls3_bikeshop import Bicycle, Wheels, Frames, Manufacturer, Bike_shop, Customer
import math
from collections import Counter
import random

def main():
    bike_shop= Bike_shop("Biped Pedalling")
    print("Welcome to "+ bike_shop.name)

    raven= Wheels("raven", 5.4, 19.9)
    thrush= Wheels("thrush", 8.6, 8.5)
    feather= Wheels("feather", 2.5, 43)

    aluminum= Frames("aluminum", 42, 130)
    carbon= Frames("carbon", 16, 352)
    steel= Frames("steel", 54, 50.7)
    frames= [aluminum, carbon, steel]

    spud_bikes= Manufacturer("Spud Bikes")
    carin_bikes= Manufacturer("Carin Bikes")


    speedster = Bicycle("speedster", random.choice(frames), spud_bikes, wheels= [raven, raven])
    vaaroom = Bicycle("vaaroom", random.choice(frames), spud_bikes, wheels= [thrush, thrush])
    cruiser = Bicycle("cruiser", random.choice(frames), carin_bikes, wheels= [raven, raven])
    mountaineer = Bicycle("mountaineer", random.choice(frames), spud_bikes, wheels= [feather, feather])
    cricket = Bicycle("cricket", random.choice(frames), carin_bikes, wheels= [thrush, thrush])
    swift = Bicycle("swift", random.choice(frames), carin_bikes, wheels= [feather, feather])

    bike_shop.stock= [speedster, speedster, speedster, vaaroom, vaaroom, vaaroom, cruiser, cruiser, mountaineer, mountaineer, cricket, cricket, swift, swift]
    inventory= Counter(bike_shop.stock)

    print("Here is our current inventory.")
    for element in inventory:
        print(element, inventory[element])

    Lily = Customer("Lily", 1000)
    Dario = Customer("Dario", 500)
    Erin = Customer("Erin", 200)

    customers= [Lily, Dario, Erin]

    for customer in customers:
        print("  ")
        print(customer.name)
        print("What's your budget? ")
        print("{} dollars.".format(customer.funds))
        print("Ok, these are the bikes in your price range.")

    
        potential_bikes= Counter(bike_shop.potential_bikes(customer))
        for bike in potential_bikes:
            print("   " + str(bike.model) + "; made by " + str(bike.manufacturer) +"   weight: " + str(bike.weight)+ " kgs " + " price:  $" + str(bike.sale_price(bike.manufacturer)))
        buying = input("Which bicycle would you like to buy? ").lower()


        for bike in bike_shop.stock:
            if bike in bike_shop.potential_bikes(customer) and buying == bike.model:
                customer.buy(bike, bike_shop)
                print(str(customer.name) + " has " + str(math.floor(customer.funds)) + " dollars left")
                print("Here is our inventory after purchase.")
                for element in Counter(bike_shop.stock):
                    print(Counter(bike_shop.stock)[element], element)
                break
        else:
            print("Hopefully we can find you a bike next time!")

if __name__ == '__main__':
    main()