class Item:
    all=[]
    def __init__(self,name:str,price:int,quantity=0):
        assert price >=0,"price must be greater than zero"
        assert quantity >=0,"quantity must be greater than zero "

        self.name=name
        self.price=price
        self.quantity=quantity
        Item.all.append(self)
    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price},{self.quantity})"
    def calculate_total_price(self):
        return self.price * self.quantity

class Phone(Item):
    all=[]
    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
        #call to supe functions .
        super().__init__(
            name,price,quantity
        )
        assert broken_phones>=0,"broken phones must be greater than zero"
        self.broken_phones=broken_phones

        Phone.all.append(self)

phone1=Phone("infinix",12000,5)
print(phone1.calculate_total_price())
phone2=Phone("nokia",8000,8)

print(Item.all)
print(Phone.all)


