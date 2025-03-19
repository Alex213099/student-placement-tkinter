"""
Python 
Fish Program 
Author :Group 7 members 
Last Modified:14/03/2025
"""
import time
import random
from datetime import datetime
print("Welcome to Otis and Othis Fish Market")

#create a dictionary of fish
fish_Types={
    "Tilapia":[150,"all year",450,"available"],
    "Nile perch":[200,"all year",350,"available"],
    "Cat fish":[160,"rainy season",250,"Available"],
    "Omena":[100,"all year",140,"available"],
    "Sardines":[140,"dry season",160,"Limited"],
    "Mud fish":[90,"rainy season",200,"Scarce"],
    "Tuna":[300,"dry season",500,"available"]
}
def months_calc(fish_dic,chosen_fish):
    current_month=datetime.now().strftime("%B")
    month=[datetime(2023 ,i ,1).strftime("%B") for i in range(1,13)]
    rainy_season=("march","april","may","september","october","november","december")
    dry_season=("january","february","june","july","august")
    tuna_season=("november","september","october","november","december","january","february","march","april")
    if  fish_dic[chosen_fish][1]=="all year":
        return "all year"
    else:
        if current_month.lower() in rainy_season:
            return ("rainy season")
        elif current_month.lower() in dry_season:
            return ( "dry season")
        elif current_month.lower() in tuna_season:
            return "nov-april"
        else:
            return "all year"

"""def apply_fishcap(fish_Types):
    if fish_Types["Nile Perch"][0]>400 or fish_Types["Tilapia"][0]>600 :
        print("The fish has a price cap in place from the kenya Fish Commision")
        return False
    else:
        return True"""

def selling_state(fish_Types,chosen_fish):
    for fish in fish_Types.keys():
        chosen_fish=chosen_fish.strip().capitalize()
      #fish that are sold while fresh
        #print(chosen_fish)
        if chosen_fish in fish:
            taken_fish=chosen_fish
            if taken_fish.capitalize() in ("Tilapia","Nile perch","Sardines","Tuna"):
                #print(taken_fish)
                return True
            else:
                # fish that are sold smoked or dried
                return False
       

#process payment 
def payment(fish_type,Chosen_fish):
    fish_details=fish_Types[Chosen_fish]
    fish_price=fish_details[0]
    fish_season=fish_details[1]
    fish_lowerpeak_price=fish_details[2]
    
    if fish_type['Tilapia'][0]>=700:
        print("Maximum price set by Kenya Fish Commission is 700")
    elif fish_type['Nile perch'][0]>=900:
        print("Maximum price set by Kenya Fish Commission is 900")
    else:
        #print(months_calc(fish_Types,Chosen_fish))
        if fish_season==months_calc(fish_Types,Chosen_fish):
            if selling_state(fish_Types,Chosen_fish)==True:
                print(f"Confirmed you have purchased {Chosen_fish} for {fish_price}.Enjoy your Fresh Fish\nVisit Again Thank you\nOtis and Othis Fish Market")
            else:
                print(f"Confirmed you have purchased {Chosen_fish} for {fish_price}.Enjoy your Smoked/Dried Fish\nVisit Again Thank you\nOtis and Othis Fish Market")
        else:
            if selling_state(fish_Types,Chosen_fish)==True:
                #print("Fish is sold Fresh")
                print(f"Confirmed you have purchased {Chosen_fish} for {fish_lowerpeak_price} Due to off peak season .Enjoy your Fresh Fish\nVisit Again Thank you\nOtis and Othis Fish Market")
            else:
                print(f"Confirmed you have purchased {Chosen_fish} for {fish_lowerpeak_price} Due to off peak season .Enjoy your Smoked/Dried Fish\nVisit Again Thank you\nOtis and Othis Fish Market")

def display_fish(fish_dic):
    for fish in fish_dic.keys():
        fish=fish.capitalize()
        
    time.sleep(1)
    print(" _____________________________________________")
    
    user_fish=""
    while(not user_fish.strip()):
         user_fish=input("Enter the fish You wish to purchase: ")
         user_fish=user_fish.capitalize().strip()

    print(user_fish)
    if user_fish in fish_dic.keys():
        print("processing request ...")
        time.sleep(1)
        payment(fish_dic,user_fish)
    else:
        print(f"Fish is not available \nTry out {random.choice(list(fish_dic.keys()))} its very Nutricious")
        display_fish(fish_dic)


if __name__=="__main__":
    #months_calc()
    display_fish(fish_Types)
