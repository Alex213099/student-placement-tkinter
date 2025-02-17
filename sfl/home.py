"""
In this program you are supposed to create a program to track the number of employeese. the day the were present for work and update their pay baesd on their attendance .
in this program the admin should be able to add new emploeey,upddate the number of days they were present and also to which location they wer
assigned to work.
"""

class Employee:
    all=[]
    def __init__(self,name:str,days_worked:int,Phone_number:str):
        self.name=name
        self.days_worked=days_worked
        self.phone_number=Phone_number
        Employee.all.append(self)

    def __repr__(self):
        return f"Employee({self.name},{self.days_worked},{self.phone_number})"

    @classmethod
    def list_employees(cls):
        for employee in cls.all:
            return employee.name ,employee.days_worked ,employee.phone_number




    
class Admin:
    all=[]
    def __init__(self,name:str,password:str,phone_number:str,):
        self.name=name
        self.password=password
        self.phone_number=phone_number
        Admin.all.append(self)

    def __repr__(self):
        return f"Admin({self.name},{self.password},{self.phone_number})"
    @classmethod
    def add_admin(cls,name:str,password:str,phone_number:str):
        new_admin=cls(name,password,phone_number)
        cls.all.append(new_admin)

    @classmethod
    def delete_admin(cls,name:str):
        for admin in cls.all:
            if admin.name==name:
                cls.all.remove(admin)
                break
    
    def add_employee(self,name:str,days_worked:int,phone_number:str):
        new_employee=Employee(name,days_worked,phone_number)
        Employee.all.append(new_employee)

    def delete_employee(self,name):
        for emp in Employee.all:
            if emp.name==name:
                Employee.all.remove(emp)
                break
    @classmethod
    def add_admin(cls,name:str,password:str,phone_number:str):
        new_admin=cls(name,password,phone_number)
        cls.all.append(new_admin)

    @classmethod
    def delete_admin(cls,name:str):
        for ad in cls.all:
            if ad.name==name:
                cls.all.remove(ad)
                break
    
    def update_days_worked(self,name:str,days__worked:int):
        for emp in Employee.all:
            if emp.name==name:
                emp.days_worked=days__worked
                break
    def update_phone_number(self,name,phone_number):
        for emp in Employee.all:
            if emp.name==name:
                emp.phone_number=phone_number
                break
    @classmethod
    def display_all_employees(cls):
        for ad in cls.all:
            return ad.name ,ad.phone_Number

        for emp in Employee.all:
            return emp.name ,emp.days_worked
class Event:
    all=[]
    def __init__(self,location,head_crew,set_up_date,Set_down_date,equips_hired=None):
        if equips_hired is None:
            equips_hired=[]
        self.location=location
        self.head_crew=head_crew
        self.set_up_date=set_up_date
        self.set_down_date=Set_down_date
        self.equips_hired=equips_hired
        Event.all.append(self)
            

    def __repr__(self):
        return f"Event( {self.location},{self.head_crew},{self.set_up_date},{self.set_down_date},{self.equips_hired})"
        
    
    @classmethod
    def add_event(cls,Location,head_crew,set_up_date,Set_down_date,Equips_hired):
        new_event=cls(Location,head_crew,set_up_date,Set_down_date,Equips_hired)
        cls.all.append(new_event)
    @classmethod
    def delete_event(cls,location):
        for event in cls.all:
            if event.location==location:
                cls.all.remove(event)
    
    @classmethod
    def list_events(cls):
        for even in cls.all:
            print(even)

    @classmethod
    def update_event(cls,location,head_crew,set_up_date,Set_down_date,equips_hired):
        for event in cls.all:
            if event.location==location:
                if head_crew is not None:
                    event.head_crew=head_crew
                if set_up_date is not None:
                    event.set_up_date=set_up_date
                if Set_down_date is not None:
                    event.set_down_date=Set_down_date
                if equips_hired is not None:
                    event.Equips_hired=equips_hired
                    break
                break

employee1=Employee("alex",5,"8888")
employee2=Employee("Kufai",10,"0705999999")

admin1=Admin("Dennis",2004,"072878798298")
admin2=Admin("Ndungu",2000,"07288201991")
print(Admin.all)

Event.add_event("Nairobi","Gichuhi","2020-2-2","2020-2-24",["terassing","stage","lights","Glass"])
print(Event.all)
print(len(Event.all))

print("______________________________________________________")
Event.delete_event("Nairobi")
print(Event.all)
print(len(Event.all))
        




