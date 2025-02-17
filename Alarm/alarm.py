"""
author:
last Date Modified:
Description:
"""
from datetime import datetime
import time
import winsound




def Get_wake_up_time():
    wake_up_time=input("Enter wake up time:").upper()
    print(f"Alarm set at: {wake_up_time}")
    return wake_up_time

def set_Alarm():
    date=datetime.now()
    date=date.strftime("%I:%M%p")
    return date


  

wake_time=Get_wake_up_time()

while True:

    current_time=set_Alarm()
    print(current_time)
    if  wake_time==current_time:
        print("Good Morning Alex Time to wake up")
        winsound.Beep(1000,5000)
        break
    else:
        break
    time.sleep(1)
"""def calculate_sleeping_time():
    retur= wake_time-current_time
    print(retur)

calculate_sleeping_time()"""
    

    