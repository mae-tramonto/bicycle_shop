import math
from collections import Counter
import random


class Bicycle(object):
    def __init__(self, model, frame, manufacturer, wheels=[]): 
        self.model= model
        self.frame= frame
        self.wheels= wheels
        self.prod_cost= wheels[0].cost *2 + frame.cost 
        self.weight= wheels[0].weight *2 + frame.weight
        self.manufacturer= manufacturer

    def __repr__(self):
        return self.model
        

class Wheels(object):
    def __init__(self, model, weight, cost): 
        self.model= model
        self.weight= weight
        self.cost= cost

    
class Frames(object):
    def __init__(self, metal, weight, cost, options= []):
        self.metal= metal
        self.weight= weight
        self.cost= cost
 
 
class Manufacturer(object):
    def __init__(self, name, bikes_made= [] ):
        self.name= name
        self.bikes_made = bikes_made
        
    def upcharge(self, bicycle):    
        price_increase = bicycle.prod_cost * 1.25
        return price_increase

    def potential_bikes(self, customer):
        affordable= []
        for bicycle in self.bikes_made:
            if self.upcharge(bicycle) <= customer.funds:
                affordable.append(bicycle)
            
        return affordable

class Bike_shop(object):
    def __init__(self, name, stock= []):
        self.name = name
        self.stock = stock
        self.computed_profit = 0

    def sale_price(self, manufacturer, bicycle):
        sale_price = manufacturer.upcharge(bicycle) * 1.4 
        return sale_price
        
    def profit(self, manufacturer, bicycle):
        profit = self.sale_price - manufacturer.upcharge(bicycle)
        return profit
        
        

class Customer(object):
    def __init__(self, name, funds, poss_bikes= []):
        self.name = name
        self.funds = funds
        self.poss_bikes = poss_bikes
        

    def buy(self, manufacturer, bike, bike_shop):
        self.poss_bikes= []
        options = manufacturer.potential_bikes(self)
        if bike in options:
            self.poss_bikes.append(bike)
            self.funds -= bike_shop.sale_price(manufacturer, bike)
            bike_shop.stock.remove(bike)
            bike_shop.computed_profit += bike_shop.profit(bike)
            print("The computed total profit after this purchase is {}.".format(math.floor(bike_shop.computed_profit)))
        
