a=5
b=0

try:
    print(a/b)
except Exception as e:
    print("you cannot divide a number by zero ", e)

print("bye")