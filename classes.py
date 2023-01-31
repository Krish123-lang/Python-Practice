class Item:

    def __init__(self, name, quantity, price) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price

    # def __str__(self) -> str:
    #     return f"Hello {self.name} "


itm_name = input("Enter the name: ")
itm_quantity = int(input("Enter the quantity: "))
itm_price = int(input("Enter the price: "))

itm = Item(itm_name, itm_quantity, itm_price)

print("********************************************************")
print(f"Item name is: {itm.name}")
print(f"Item quantity is: {itm.quantity}")
print(f"Item price is: {itm.price}")
# print(itm)
print("********************************************************")

total = itm.quantity * itm.price
print(f"Total: {total} ")
