from item import Item

item1 = Item("MyItem", 750)

item1.__name = "AnotherName"
print(item1.name)
