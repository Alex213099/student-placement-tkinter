#encapsulation.
class Item:
    payrate=0.8 #the pay rate after 20% discount.
    all=[]

    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0,f"price {price} is not greater than or equal to zero "
        assert quantity>=0,f"quantity {quantity} is not equal to or greater than zero"
    
        self.name=name
        self.__price=price
        self.quantity=quantity

        Item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    def __repr__(self):
        return f"Item( '{self.name}' ,{self.__price} , {self.quantity} "

    def calculate_total_price(self):
        return self.__price*self.quantity
    
    def apply_discount(self):
        self.__price= self.__price * self.payrate

    def apply_increment(self,increment_value):
        self.__price= self.__price+self.__price*increment_value

    def __connect_to_smtp(self):
        pass

    def __write_body(self):
        return f"""
        hello {self.name} the price is {self.__price} and the quantity is {self.quantity}
        Regards, Alex Gitonga
        """
    def __send(self):
        pass

    def send_email(self):
        self.__connect_to_smtp()
        self.__write_body()
        self.__send()


item1=Item("sugar",1000)
print(item1.price)
item1.apply_increment(0.2)
print(item1.price)
item1.apply_discount()
print(item1.price)

item1.send_email()
 