import sys
a=700
b=3.7
c=4+2j
d="Hello"
e=[20,30,60]
f=(20,30,60)
g={20,30,60}
h={"A":20,"B":30,"C":60}
print(type(a))
print(type(b))
print(type(c))

print(id(d))
print(hex(id(a)))
print(sys.getsizeof(d)," bytes")
print(sys.getsizeof(h)," bytes")


