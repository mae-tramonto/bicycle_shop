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
    
    # def weight_compute(self, frame, wheel):
    #     weight= frame.weight + (wheel.weight * 2)
    #     return weight
        
    # def prod_cost(self, frame, wheel):
    #     prod_cost= frame.cost + (wheel.cost * 2)
    #     return prod_cost
        
        

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
        
    def upcharge(self, bicycle):    
        upcharge = bicycle.prod_cost * 1.25
        return upcharge


class Bike_shop(object):
    def __init__(self, name, stock= []):
        self.name = name
        self.stock = stock
        self.computed_profit = 0
        
    def sale_price(self, manufacturer):
        sale_price = manufacturer.upcharge * 1.4 
        return sale_price
        
    def profit(self, manufacturer):
        profit = self.sale_price(manufacturer) - manufacturer.upcharge
        return profit
        
        

class Customer(object):
    def __init__(self, name, funds, poss_bikes= []):
        self.name = name
        self.funds = funds
        self.poss_bikes = poss_bikes
        
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
            print("The computed total profit after this purchase is {}.".format(math.floor(bike_shop.computed_profit)))
        
