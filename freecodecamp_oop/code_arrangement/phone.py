from item import Item
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



