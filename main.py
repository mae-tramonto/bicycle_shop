from ls3_bikeshop import Bicycle, Wheels, Frames, Bike_shop, Customer
import math
from collections import Counter
import random

def main():
    bike_shop= Bike_shop("Biped Pedalling")
    print("Welcome to "+ bike_shop.name)
    
    raven= Wheels("raven", 5.4, 44.9)
    thrush= Wheels("thrush", 8.6, 15.5)
    feather= Wheels("feather", 2.5, 62)
    
    aluminum= Frames("aluminum", 42, 199.99)
    carbon= Frames("carbon", 16, 320)
    steel= Frames("steel", 54, 80.7)
    
    speedster = Bicycle("speedster", random.choice(Frames.options), random.choice(Wheels.options))
    vaaroom = Bicycle("vaaroom", random.choice(Frames.options), random.choice(Wheels.options))
    cruiser = Bicycle("cruiser", random.choice(Frames), random.choice(Wheels))
    mountaineer = Bicycle("mountaineer", random.choice(Frames), random.choice(Wheels))
    cricket = Bicycle("cricket", random.choice(Frames), random.choice(Wheels))
    swift = Bicycle("swift", random.choice(Frames), random.choice(Wheels))
    
    Frames.options= [aluminum, carbon, steel]
    
    Wheels.options= [raven, thrush, feather]
    
    bike_shop.stock= [speedster, speedster, speedster, vaaroom, vaaroom, vaaroom, cruiser, cruiser, mountaineer, mountaineer, cricket, cricket, swift]
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
        
        
        potential_bikes= Counter(customer.potential_bikes(bike_shop))
        for bike in potential_bikes:
            print("   " + str(bike.model) + ";   weight: " + str(bike.weight)+ " kgs " + " price:  $" + str(bike_shop.sale_price(bike)))
        buying= input("Which bicycle would you like to buy? ").lower()
        
        for bike in customer.potential_bikes(bike_shop):
            if bike in customer.potential_bikes(bike_shop) and buying == bike.model:
                customer.buy(bike, bike_shop) 
                print(str(customer.name) + " has " + str(math.floor(customer.funds)) + " dollars left")
                print("Here is our inventory after purchase.")
                for element in Counter(bike_shop.stock):
                    print(Counter(bike_shop.stock)[element], element)
                #print(str(bike_shop.stock.count(bike)) + " " + bike.model)
                break
           
        else: 
            print("Hopefully we can find you a bike next time!")    
                
                   
                
    
    
    
    
if __name__ == '__main__':
    main()