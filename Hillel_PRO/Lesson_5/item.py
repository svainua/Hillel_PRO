import csv


class Item:
    pay_rate = 0.8  # The pay after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert (
            quantity >= 0
        ), f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value    


    @property
    # Property decorator : Read file only. Protects from changes
    def name(self):
        return self.__name   

    @name.setter
    # Allows to change
    def name(self, value):
        self.__name = value 

    def calculate_total_price(self):
        return self.__price * self.quantity


    @classmethod
    def instanciate_from_csv(cls):
        with open("items.csv", "r") as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero.
        # For i.e. 5.0, 100.0
        if isinstance(num, float):
            # Count out the floats that are point zero.
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False    

    def __repr__(self):
        return f"{self.__class__.__name__}"
        f"('{self.name}', {self.__price}, {self.quantity})"




# Item.instanciate_from_csv()
# print(Item.all)

# item_1 = Item("Phone", 100, 1)
# item_2 = Item("Laptop", 1000, 3)
# item_3 = Item("Cable", 10, 5)
# item_4 = Item("Mouse", 50, 5)
# item_5 = Item("Keyboard", 75, 5)

# print(item_1.calculate_total_price())
# print(item_2.calculate_total_price())

# print(Item.__dict__) # All the attrributes for Class method
# print(item_1.__dict__) # All the attrributes for Class method

# print(item_1.apply_discount())

# item_2.pay_rate = 0.5
# print(item_2.apply_discount())

# for instance in Item.all:
#     print(instance.name)
        
        
