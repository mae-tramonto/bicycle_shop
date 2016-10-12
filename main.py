from ls3_bikeshop import Bicycle, Bike_shop, Customer

def main():
    bike_shop= Bike_shop("Biped Pedalling")
    print("Welcome to "+ bike_shop.name)
    
    speedster = Bicycle("speedster", 24.8, 324)
    vaaroom = Bicycle("vaaroom", 36.2, 150)
    cruiser = Bicycle("cruiser", 43.5, 125)
    mountaineer = Bicycle("mountaineer", 38.1, 224)
    cricket = Bicycle("cricket", 22.5, 547)
    swift = Bicycle("swift", 18.2, 824)
    
    bike_shop.stock= [speedster, vaaroom, cruiser, mountaineer, cricket, swift]

    Lily = Customer("Lily", 1000)
    Kofi = Customer("Kofi", 500)
    Erin = Customer("Erin", 200)

    customers= [Lily, Kofi, Erin]
    
    for customer in customers:
        print("  ")
        print(customer.name)
        print("What's your budget? ")
        print("{} dollars.".format(customer.funds))
        print("Ok, these are the bikes in your price range.")
        
        for bike in customer.potential_bikes(bike_shop):
            print("   " + bike.model, bike_shop.sale_price(bike))
            
        buying= input("Which bicycle would you like to buy? ").lower()
        if bike in customer.potential_bikes(bike_shop) == buying.lower():
            customer.buy(bike, bike_shop) 
            print(str(customer.name) + " has " + str(customer.funds) + " dollars left")
            #print(bike_shop.stock) 
            print(customer.poss_bikes)
        else:
            print("Hopefully we can find you a bike next time!")    
    
    
    
    
if __name__ == '__main__':
    main()