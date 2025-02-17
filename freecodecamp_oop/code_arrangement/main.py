from item import Item
from phone import Item

item1=Item("microwave",3000,8)
item2=Item("ironboard",7000,8)
item3=Item("television",9982,7)


item1.read_only_name

#print(item1.__name)
print(item1.name)
item1.name="pasi"

print(item1)
#sometimes you do not want to change the name of the attributes.