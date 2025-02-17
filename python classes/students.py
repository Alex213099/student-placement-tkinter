class students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def get_grade(self,):
        return self.grade
    
class course:
    def __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]

    def add_students(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average(self):
        value=0
        for student in self.students:
            value+=students.get_grade()
            return value/ len(self.students)

s1=students("Alex",21,90)
s2=students("Kamau",20,55)
s3=students("gitonga",18,80)


course1=course("science", 2)
course1.add_students(s1)
course1.add_students(s2)


print(course1.students[0])
print(course.get_average())
