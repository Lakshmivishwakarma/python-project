class Inventory:
    def __init__(self, dictionary):
        self.dict = dictionary

    def add_product(self, product_name, product_count):
        if product_name in self.dict:
            self.dict[product_name] += product_count
            print(self.dict)
        else:
            self.dict[product_name] = product_count
            print(self.dict)

    def remove_product(self, product_name):
        if product_name in self.dict:
            del (self.dict[product_name])
            print(self.dict)

    def decrease_prod_count(self, product_name, count):
        if product_name in self.dict:
            if self.dict[product_name] >= count:
                self.dict[product_name] -= count
                print(self.dict)
            else:
                print("count will not be greater then remaining product count")


mobile_inventory = Inventory({"samsung": 1, "redmi": 7, "nokia": 5})
print(str(mobile_inventory.dict))

mobile_inventory.add_product("apple", 2)

mobile_inventory.remove_product("nokia")

mobile_inventory.decrease_prod_count("redmi", 8)

