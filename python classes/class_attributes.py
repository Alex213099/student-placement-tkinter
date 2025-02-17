class person:
    number_of_people =0

    def __init__(self,name):
        self.name=name
        person.number_of_people+=1

p1=person("Irene")
print(person.number_of_people)
p2=person("joan")
print(person.number_of_people)

