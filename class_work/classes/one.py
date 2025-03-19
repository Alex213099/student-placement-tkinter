from abc import ABC ,abstractmethod
class Shape(ABC):
    @abstractmethod
    def show(self):
        pass


class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def __str__(self):
        return f"Student()"
    
    def show(self):
        print("The Area of the rectangle : ", self.length*self.width)
l=eval(input("enter the length \n"))
w=eval(input("enter the value for the width \n"))
student1=Rectangle(l,w)
student1.show()
#instance variables is where a variable belongs to a specific object
#class variables is where a avraiable belongs to the class and all instances of a class

class Triangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def show(self):
        print("The area of the triangle is ",self.length*self.width*0.5)

tri=Triangle(l,w)
tri.show()
#create a GUI form for excercise .product code , product name , product desc , product price , product quantity

#abstraction is the process of hiding implementation details . and only showing the 


