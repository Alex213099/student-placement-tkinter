class pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"i am a {self.name} and i am {self.age} years old")

    def speak(self):
        print("I dont know what to say")


class Dog(pet):
    def speak(self):
        print("BARK")

class cat(pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color

    def speak(self):
        print("meow")
    def show(self):
        print(f"i am {self.name} and i am {self.age} years old and i am {self.color}")

p=pet("tim",19)
p.show()

c=cat("puss",21,"blue")
c.show()
c.speak()

d =Dog("poppy",12)
d.show()
d.speak()
p.speak()