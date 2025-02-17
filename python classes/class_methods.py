class person:
    number_of_people=0

    def __init__(self,name):
        self.name=name
        person.add_number_of_people()

    @classmethod
    def number_of_people(cls):
        return cls.number_of_people
    
    @classmethod
    def add_number_of_people(cls):
        cls.number_of_people +=1

p1=person("joan")
p2=person("Irene")

print(person.number_of_people)

