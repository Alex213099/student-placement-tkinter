"""
Class dog and its methods are created and instances created afterwards.
"""

class Dog:
    def bark(self):
        print("bark woof woof ")
    
    def add_one(self, x):
        return x+1

d=Dog()
d.bark()

eight=d.add_one(7)

print(type(Dog))
print(eight)