def add_item():
    
    while True:
        item = input("Enter the name of the item to add : ")
        price = input("Enter the price of the item: ")
        
        with open("menu.txt", "a") as file:
            file.write(f"{item.ljust(20 - len(item))} - ${price}\n")
        
        print(f"{item} has been added to the menu.")
        
        choice = input("Do you want to add more items? (y/n): ").casefold()
        if choice == "n":
            break