"""
Author :Group & members
Last date modified:15/03/2025
description:Simple matatu fare app

"""
import time
from datetime import datetime 
Route={
    'Route':"Morning,Afternoon,Evening",
    "1.CBD-Thika":"100,60,100",
    "2.CBD-Kiambu":"80,30,100",
    "3.Kiambu-CBD":"70,50,30",
    "4.Thika-CBD":"120,60,60",
    "5.Westlands-CBD":"130,60,60",
    "6.CBD-westlands":"30,50,120",
    "7.CBD-Githurai":"30,50,40",
    "8.Githurai-CBD":"70,40,50"

}
def get_time():
    #currenttime=datetime.now().strftime("%I,%M,%p")
    period=datetime.now().strftime("%p")
    hour=int(datetime.now().strftime("%I"))
    if period=="AM" and hour<=12 :
        return "morning"
    elif period=="PM" and hour<=12 and hour <6:
        return "afternoon"
    else:
        return "evening"


def calculate_fare(route,chosenroute):
    
    for rou in route.keys():
        modified_rou=rou[2:]
        print(modified_rou)
        print(chosenroute)
        if modified_rou ==chosenroute:
            time=get_time()
            if time =="morning":
                print(route[chosenroute][0])
            elif time=="afternoon":
                print(route[chosenroute][1])
            else:
                print(route[chosenroute][2])
            break
        else:
            print("???")
  

def display_routes(route):
    for key in route.keys():
        print(key)

    choice=None
    try:
        choice=int(input("Enter your choice please"))
        if choice not in range(1,9):
            print("Invalid choice")
            choice=None
            display_routes(route)
        else:
            pass
            
    except ValueError as err:
        print("Enter only numbers please")
        choice=None
        display_routes(route)
    if choice==1:
        return "CBD-Thika"
    elif choice==2:
        return "CBD-Kiambu"
    elif choice==3:
        return "Kiambu-CBD"
    elif choice==4:
        return "Thika-CBD"
    elif choice==5:
        return "Westlands-CBD"
    elif choice==6:
        return "CBD-westlands"
    elif choice==7:
        return "CBD-Githurai"
    elif choice==8:
        return "Githurai-CBD"
    else:
        return "route no found"

chosenroute=display_routes(Route)
fare=calculate_fare(Route,chosenroute)
    


"""if __name__=="__main__":
    print("Welcome to Gitosh Trans")
    time.sleep(1)
    chosenroute=display_routes(Route)"""

    
    