"""
it is always important to close a connection after code .therefore lets see how can do this using try and except.
"""
a=5
b=0

try:
    print("resource open")
    a/b
    

except Exception as e:
    print("you cannot divide by zero", e)

finally:
    print("resource closed")
