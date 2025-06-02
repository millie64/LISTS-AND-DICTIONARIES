inventory={"mangoes":{"price":25, "stock":15},
"onions":{"price":10, "stock":40}, 
"tomatoes":{"price":10, "stock":100}, 
"cabbages":{"price":120, "stock":8}}
items = input("Which item do you want to check up? ").strip().lower()
if items in inventory:
    print(f"We have {items} and the price is {inventory[items]['price']}")
else:
    new_item = input("Would you like to add the item? (yes/no) ").strip().lower()
    if new_item == "yes":
        add_price = int(input(f"Please add it's price" ))
        inventory[new_item]=add_price
        new_stock = int(input("How many do you want to add? "))
        if new_stock:
            print(f"The {items} costs {add_price} and they are {new_stock} in stock.")
    else:
        print("Sorry, we don't have that.")
print(inventory)
    
