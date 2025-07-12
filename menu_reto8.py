from typing import List

class MenuItem:
    def __init__(self, name:str, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.specific_discount:float = 0
    
    def change_discount(self,new_discount:float):
        if(new_discount < 1 and new_discount >= 0):
            self.specific_discount = new_discount
    
    def price_total(self)->float:
        return self.price*self.quantity
    
    def __str__(self):
        return f"{self.name}: {self.price}$"

class Appetizer(MenuItem):
    def __init__(self, name:str, price:float, quantity:int, size:str):
        super().__init__(name, price, quantity)
        self.size = size

class Drink(MenuItem):
    def __init__(self, name:str, price:float, quantity:int, type:str):
        super().__init__(name, price, quantity)
        self.type = type

class MainCourse(MenuItem):
    def __init__(self, name:str, price:float, quantity:int, vegetarian:bool, 
                family_size:bool):
        super().__init__(name, price, quantity)
        self.vegetarian = vegetarian
        self.family_size = family_size

class Dessert(MenuItem):
    def __init__(self, name:str, price:float, quantity:int, size:str):
        super().__init__(name, price, quantity)
        self.size = size

#Menu
bruschetta = Appetizer("Bruschetta", 8, 1, "Medium")
cheese_nachos = Appetizer("Cheese Nachos", 10, 1, "Large")
coca_cola = Drink("Coca Cola", 3, 1, "Soda")
orange_juice = Drink("Orange Juice", 4, 1, "Natural")
coffee = Drink("Coffee", 5, 1, "Hot")
alfredo_pasta = MainCourse("Alfredo Pasta", 15, 1, True, False)
burger = MainCourse("Burger", 12, 1, False, False)
family_grill = MainCourse("Family Grill", 35, 1, False, True)
chocolate_cake = Dessert("Chocolate Cake", 6, 1, "Medium")
vanilla_ice_cream = Dessert("Vanilla Ice Cream", 4, 1, "Small")
cheesecake = Dessert("Cheesecake", 7, 1, "Large")
caesar_salad = MainCourse("Caesar Salad", 10, 1, True, False)

#Discount
bruschetta.change_discount(0.15)
cheese_nachos.change_discount(0.17)
cheesecake.change_discount(0.20)


"""
order class with its iterable
"""
class Order:
    def __init__(self):
        self.list_order = []
    
    def add_item_menu(self, new_item:MenuItem):
        if(is_instance(new_item, MenuItem)):
            self.list_order.append(new_item)
        else:
            print("the element is not a MenuItem")
    
    def __iter__(self):
        return MenuIterator(self.list_order)
    
    def total_bill_amount(self)->float:
    total = sum(
        item.price_total() * (1 - item.specific_discount)
        for item in self.list_order
    )
    return total

    def __str__(self):
    print_code = "Order:\n"
    for i, item in enumerate(self.list_order, 1):
        print_code += f" ({i}). {item}"
        if item.specific_discount != 0:
            print_code += f" (-{item.specific_discount * 100:.0f}%)"
        print_code += "\n"
    print_code += f"\n --> Account total: {self.total_bill_amount():.2f}$"
    return print_code

    def deliver_order(self):
        if item.quantity != 0 for item in self.list_order:
            for item in self.list_order:
                print(f"order delivered: {item.name}")
                item.quantity -= 1
        else:
            print("it is not possible to deliver the order")



class OrderIterator:
    def __init__(self, list_order):
        self.list_order = list_order
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.list_order) and list_order[index].quantity != 0:
            item_order = list_order[self.index]
            self.index += 1
            return item_order
        else:
            raise StopIteration


##Test
orden = Order()
orden.add_item_menu(bruschetta)
orden.add_item_menu(coffee)
orden.add_item_menu(cheesecake)

print(orden)

print("\nItems iterados en orden:")
for item in orden:
    print(f"- {item.name} ({item.quantity} unidades disponibles)")

orden.deliver_order()

for item in orden:
    print(f"{item.name} → {item.quantity} unidades restantes")
