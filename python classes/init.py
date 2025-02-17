"""
The init method is instatiated every time a new object is created from a class
"""

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self,age):
        self.age=age


d=Dog("tim",10)
d2=Dog("Bosco",13)

print(d.get_name())
print(d2.get_name())

print(d.get_age())
print(d2.get_age())

d.set_age(20)
d2.set_age(40)
print(d.get_age())
print(d2.get_age())