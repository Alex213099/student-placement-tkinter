class Products:
    all=[]
    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0,"price must be greater than zero"
        assert quantity>=0,"quantity must be greater than zero"

        self.name=name
        self.price=price
        self.quantity=quantity
        Products.all.append(self)

    def __repr__(self):
        return f"Products('{self.name}', {self.price},{self.quantity})"
    
    
    def display_product(self):
        for product in Products.all:
            print(product.name , "  " , product.price)
            
    

    def add_product(self,name,price,quantity):
       newp=Products(name,price,quantity)
       Products.all.append(newp)

    def delete_product(self,name):
        for product in Products.all:
            if product.name ==name:
                Products.all.remove(product)
            else:
                print("product not found")
    
    
        

class Customers:
    good_credited=[]
    all=[]
    def __init__(self,name:str,is_customer:bool,credit_amount=0):
        assert credit_amount>0,"credit balance cannot be less than zero"

        self.name=name
        self.is_customer=is_customer
        self.credit_amount=credit_amount
        self.product_owing=[]

        Customers.all.append(self)

    def __repr__(self):
        return f"Customers '{self.name}', {self.is_customer}, {self.credit_amount}"
    
    def display_customers(self):
        print( "name " ,"credit amount ", " is customer?")
        for customer in Customers.all:
            print(customer.name, " ",customer.credit_amount," ",customer.is_customer)
    
    def buy_goods_on_credit(self,product):
        total_debt=0
        if total_debt>=self.credit_amount:
            return False
        else:
            self.product_owing.append(product)
            total_debt+=product.price
            print(self.product_owing)
            print(total_debt)

            
    
    def pay_debt(self,product):
        total_debt=0
        self.product_owing.remove(product)
        total_debt-=product.price
        print(self.product_owing)
        print(total_debt)

        
    def show_goods_Credited(self):
        return self.product_owing
   
product1=Products("bread",65,16)
product2=Products("rice",200,14)
product3=Products("milk",60,20)



customer1=Customers("Alex",True,2000)
customer2=Customers("peter",True,4000)
customer3=Customers("gichuhi",False,10)

print("products Available")
product1.display_product()


print(customer1.display_customers())

customer1.buy_goods_on_credit(product1)
customer1.buy_goods_on_credit(product2)
customer1.pay_debt(product2)
customer1.buy_goods_on_credit(product3)

print(customer1.product_owing)