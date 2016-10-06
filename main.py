from ls3_bikeshop import Bicycle, Bike_shop, Customer
def main():
    bike_shop= Bike_shop("Biped Pedalling")
    print("The shop is called "+ bike_shop.name)
    
    Vaaroom = Bicycle("Vaaroom", 36.2, 150)
    Speedster = Bicycle("Speedster", 24.8, 324)
    Cruiser = Bicycle("Cruiser", 43.5, 124)
    Mountaineer = Bicycle("Mountaineer", 38.1, 224)
    Cricket = Bicycle("Cricket", 22.5, 546)
    Swift = Bicycle("Swift", 18.2, 824)
    
    bike_shop.stock= [Vaaroom, Speedster, Cruiser, Mountaineer, Cricket, Swift]

    Erin = Customer("Erin", 200)
    Kofi = Customer("Kofi", 500)
    Lily = Customer("Lily", 1000)

    customers= [Erin, Kofi, Lily]
    
    print("Welcome to {}! What are you looking for today? ".format(bike_shop.name))
    for customer in customers:
        print(customer.name)
        print("What's your budget? ")
        print("{} dollars.".format(customer.funds))
        print("Ok, these are the bikes in your price range.")
        
        for bike in customer.potential_bikes(bike_shop):
            print(bike.model)
            # buy_bike = input("Which bicycle would you like to buy? ").lower()
            # if bicycle in Customer.potential_bikes() == buy_bike.lower():
            #     Customer.buy()
        
    
if __name__ == '__main__':
    main()