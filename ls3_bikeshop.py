
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

    def sale_price(self, manufacturer):
        sale_price = manufacturer.upcharge(self) * 1.4
        return sale_price

    def __repr__(self):
        return self.model

class Wheels(object):
    def __init__(self, model, weight, cost):
        self.model= model
        self.weight= weight
        self.cost= cost

    def __repr__(self):
        return self.model

class Frames(object):
    def __init__(self, metal, weight, cost, options= []):
        self.metal= metal
        self.weight= weight
        self.cost= cost

class Manufacturer(object):
    def __init__(self, name):
        self.name= name

    def upcharge(self, bicycle):
        price_increase = bicycle.prod_cost * 1.25
        return price_increase

    def __repr__(self):
        return self.name

class Bike_shop(object):
    def __init__(self, name, stock= []):
        self.name = name
        self.stock = stock
        self.computed_profit = 0

    def potential_bikes(self, customer):
        affordable = []
        for bicycle in self.stock:
            if bicycle.sale_price(bicycle.manufacturer) <= customer.funds:
                affordable.append(bicycle)
        return affordable

    def profit(self, manufacturer, bicycle):
        profit = bicycle.sale_price(manufacturer) - manufacturer.upcharge(bicycle)
        return profit

    def __repr__(self):
        return self.name

class Customer(object):
    def __init__(self, name, funds, poss_bikes= []):
        self.name = name
        self.funds = funds
        self.poss_bikes = poss_bikes

    def buy(self, bike, bike_shop):
        options = bike_shop.potential_bikes(self)
        if bike in options:
            self.poss_bikes.append(bike)
            self.funds -= bike.sale_price(bike.manufacturer)
            bike_shop.stock.remove(bike)
            bike_shop.computed_profit += bike_shop.profit(bike.manufacturer, bike)
            print("The computed total profit after this purchase is {}.".format(math.floor(bike_shop.computed_profit)))