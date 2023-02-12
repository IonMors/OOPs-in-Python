from item import Item
#from phone import Phone

#Item.instantiate_from_csv()
#print(Item.all)

item1 = Item("MyItem", 750, 5)

# Setting an attribute
item1.name = "Othername"

# Getting an Attribute
print(item1.name)
