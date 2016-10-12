
class Bicycle(object):
    def __init__(self, model, weight, prod_cost):
        self.model= model
        self.weight= weight
        self.prod_cost= prod_cost


    
class Bike_shop(object):
    def __init__(self, name, stock= []):
        self.name = name
        self.stock = stock
        self.computed_profit = 0
        
    def sale_price(self, bicycle):
        sale_price = bicycle.prod_cost * 1.2 
        return sale_price
        
    def profit(self, bicycle):
        profit = self.sale_price(bicycle) - bicycle.prod_cost
        return profit
        
        

class Customer(object):
    def __init__(self, name, funds, poss_bikes= []):
        self.name = name
        self.funds = funds
        self.poss_bikes = poss_bikes
        
    # def funds(self):
    #     self.funds - sale_price(bicycle)
    def potential_bikes(self, bike_shop):
        affordable= []
        for bicycle in bike_shop.stock:
            if bike_shop.sale_price(bicycle) <= self.funds:
                affordable.append(bicycle)
            
        return affordable

    def buy(self, bike, bike_shop):
        self.poss_bikes= []
        options = self.potential_bikes(bike_shop)
        if bike in options:
            self.poss_bikes.append(bike)
            self.funds -= bike_shop.sale_price(bike)
            bike_shop.stock.remove(bike)
            bike_shop.computed_profit += bike_shop.profit(bike)
            print("The computed profit after this purchase is {} .".format(bike_shop.computed_profit))

