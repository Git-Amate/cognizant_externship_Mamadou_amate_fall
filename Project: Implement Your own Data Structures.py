print("Welcome to the Inventory Manager!")

boucle = True

inventory ={
"apple": (10, 2.5),
"banana": (20, 1.2)
}

while boucle:
    print("What do you wanna do today ? \n")
    choice = int(input("1 - Display the inventory \n"
          "2 - adding new item to the inventory \n"
          "3 - Remove an item from the inventory \n"
          "4 - Update the quantity or price of an existing item \n"
                       "5 - leave \n"))

    if choice == 1:
        for key,value in inventory.items():
            print(f"item : {key} quantité : {value[0]} price : {value[1]} \n")


    if choice == 2:
        while True:
            item_added = input("Please enter the name of the item you want to add: ").strip()
            already_exists = False

            for key in inventory.keys():
                if item_added.lower() == key.strip().lower():
                    print("The item already exists!")
                    already_exists = True
                    break

            if not already_exists:
                break

        item_added_quantity = int(input("please put the quantity of the item you want to add "))
        item_added_price = int(input("please put the price of the item you want to add "))
        inventory.update({item_added.lower():(item_added_quantity,item_added_price)})
        print("item saved !\n")


    if choice == 3:
        for key,value in inventory.items():
            print(f"item : {key} quantité : {value[0]} price : {value[1]} \n")

        while True:
            item_to_delete = input("put the name of the item you want to remove ")
            exists = False

            for key in inventory.keys():
                if item_to_delete.lower() == key.strip().lower():
                    exists = True
                    break

            if exists:
                break
            else:
                print("The item doesn't exist! Please enter an existing item.")


        del inventory[item_to_delete.lower()]
        print(f"item {item_to_delete} is removed")


    if choice == 4:
        for key,value in inventory.items():
            print(f"item : {key} quantité : {value[0]} price : {value[1]} \n")

        while True:
            item_to_update = input("Please enter the name of the item you want to update: ").strip()
            exists = False

            for key in inventory.keys():
                if item_to_update.lower() == key.strip().lower():
                    exists = True
                    break

            if exists:
                break
            else:
                print("The item doesn't exist! Please enter an existing item.")

        print(f"the actual price of {item_to_update.lower()} is {inventory[item_to_update.lower()][1]} and the quantity is {inventory[item_to_update.lower()][0]} ")
        item_to_update_price = int(input(f"put the new price of the {item_to_update}"))
        item_to_update_quantity = int(input(f"put the new quantity of the {item_to_update}"))
        inventory.update({item_to_update:(item_to_update_quantity,item_to_update_price)})
        print(f"item {item_to_update} is updated")

    if choice == 5:
        print("thank you see you next time !")
        boucle = False
        break





