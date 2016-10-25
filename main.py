from ls3_bikeshop import Bicycle, Bike_shop, Customer
import math
from collections import Counter

def main():
    bike_shop= Bike_shop("Biped Pedalling")
    print("Welcome to "+ bike_shop.name)
    
    speedster = Bicycle("speedster", 24.8, 324)
    vaaroom = Bicycle("vaaroom", 36.2, 150)
    cruiser = Bicycle("cruiser", 43.5, 125)
    mountaineer = Bicycle("mountaineer", 38.1, 224)
    cricket = Bicycle("cricket", 22.5, 547)
    swift = Bicycle("swift", 18.2, 824)
    
    
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