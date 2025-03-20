"""
Author :Alex Gitonga
Last date modified:19/03/2025
description:Program to calculate students scores 
"""
import statistics
marks=list()
def getmarks(y):
    while True:
        try:
            number_subject=int(input("Enter the number of subject you are doing: "))
            if number_subject<0:
                print("You have entered number less than zero")
            else:
                break
        except ValueError as err:
            print("Invalid Entry enter only numbers")

    while len(y)< number_subject:
        try:
            mark=int(input("Enter the mark you scored for the subject: "))
            while mark<0 or mark>100:
                print("The value you entered should be between 0 -100")
                mark=int(input("Enter the mark you scored: "))
            y.append(mark)
        except ValueError as err:
            print("Enter only numbers please")
    return y



"""def validate_mark():
    while True:
        try:
            mark =int(input("Enter the mark you scored"))
            if mark <0 or mark >100:
                print("Mark is not in the desired range ")
                validate_mark()

            elif mark is None:
                validate_mark()

            elif not isinstance(mark, int):
                print("Enter only intergers")
                validate_mark()

            else:
                return True 
            
        except ValueError as e:
            print("_____-")
            validate_mark()

"""

def get_total(tuple_marks):
    total=0
    for i in tuple_marks:
        total+=i
    return total

def number_of_scores(tuple_marks):
    return len(tuple_marks) 

def highest_score(tuple_marks):
    highest=0
    for i in tuple_marks:
        if i>highest:
            highest=i
    return highest

def lowest_score(tuple_marks):
    lowest=100
    for i in tuple_marks:
        if i<lowest:
            lowest=i
    return lowest

def get_average():
    total=get_total(tuple_marks)
    number=number_of_scores(tuple_marks)
    average=total/number
    average=round(average,2)
    return average

def get_standarddeviation(tuple_marks):
    stddev=statistics.stdev(tuple_marks)
    stddev=round(stddev,2)
    return stddev

def get_grade(i):
    #for i in tuple_marks:
    if i>=0 and i<=39:
        return 'E'
    elif i>=40 and i<=49:
        return 'D'
    elif i>=50 and i<=59:
        return 'C'
    elif i>=60 and i<=69:
        return 'B'
    elif i>=70 and i<=100:
        return 'A'
    else:
        return "Something went wrong"
def display_scores():
    total =get_total(tuple_marks)
    size_tuple=number_of_scores(tuple_marks)
    high=highest_score(tuple_marks)
    low=lowest_score(tuple_marks)
    average=get_average()
    stddeviation=get_standarddeviation(tuple_marks)

    print(f"Your Total Score is {total}\n")
    print(f"Total numbers of scores {size_tuple} \n")
    print(f"The highest mark earned is {high} \n")
    print(f"The lowest mark earned is {low}\n")
    print(f"The average of the scores is {average} \n")
    print(f"The standard deviation is {stddeviation}\n")

    for i in tuple_marks:
        grade=get_grade(i)
        print(f"The grade scored for score {i} {grade} ")


if __name__=="__main__":
    print("Welcome To this Program \n")
    print("proceed to enter your marks please \n")
    tuple_marks=getmarks(marks)
    display_scores()


    

            
