def add_number(num1,num2):

    try:
        if isinstance(num1,int)or isinstance(num1,float)and isinstance(num2,int)or isinstance(num2,float):
            return num1+num2
        else:
            raise Exception("only intergers and float only")
    except Exception as e :
        return e
    except ZeroDivisionError:
        return("zero division error")
    else:
        print("no error")



print(add_number(3,2))
print(add_number(8,2))
print(add_number(7,1))
print(add_number(6,9))
print("execution completed")

#a user can define their own exception using raiseexception