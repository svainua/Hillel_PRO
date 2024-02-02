from item import Item

item1 = Item("MyItem", 750, 6)

item1.apply_increment(0.2)
item1.apply_discount()

print(item1.price)
