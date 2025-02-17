import csv
class Item:
    all=[]
    def __init__(self,name:str,price:int,quantity=0):
        assert price >=0,"price must be greater than zero"
        assert quantity >=0,"quantity must be greater than zero "

        self.__name=name
        self.price=price
        self.quantity=quantity
        Item.all.append(self)
    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price},{self.quantity})"
    def calculate_total_price(self):
        return self.price * self.quantity
    @property
    def read_only_name(self):
        return "AAA"
    @property
    def name (self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value
        