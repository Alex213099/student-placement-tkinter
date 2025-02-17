import  csv
class Item:
    payrate=0.8 #the pay rate after 20% discount.
    all=[]

    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0,f"price {price} is not greater than or equal to zero "
        assert quantity>=0,f"quantity {quantity} is not equal to or greater than zero"
    
        self.name=name
        self.price=price
        self.quantity=quantity

        Item.all.append(self)

    def __repr__(self):
        return f"Item( '{self.name}' ,{self.price} , {self.quantity} "

    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price= self.price * self.payrate

    @classmethod
    def instatiate_from_csv(cls):
        """with open("C:\Users\alexk\Desktop\python_projects\freecodecamp_oop\items.csvs","r") as f:
            reader= csv.DictReader(f)
            items=list(reader)

        for item in items:
            print(item)"""
    @staticmethod    
    def is_interger(num):
        #we will count out the decimals that are point zero.

        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False



