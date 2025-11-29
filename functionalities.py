def add_item(menu_item):
    
    while True:
        item = input("Enter the name of the item to add : ")
        price = input("Enter the price of the item: ")
        
        menu_item.update({item: price})
        
        with open("menu.txt", "a") as file:
            file.write(f"{item.ljust(20)} - ${price}\n")
        
        print(f"{item} has been added to the menu.")
        
        choice = input("Do you want to add more items? (y/n): ").casefold()
        if choice == "n":
            break
    return menu_item

def display_menu():
    
    print("Menu:\n")
    
    with open("menu.txt", "r") as file:
        for line in file:
            print(line.strip())
        
    print("\n")

def update_menu(menu_item):
    display_menu()
    
    update_item = input("Enter the item to update: ").strip()
    new_price = input("Enter the item's new price: ").strip()
    
    menu_item[update_item] = new_price
    
    with open("menu.txt", "w") as file:
        for item, price in menu_item.items():
            file.write(f"{item.ljust(20)} - ${price}\n")
    
    print(f"{update_item}'s price has been updated to ${new_price}.")

def delete_item(menu_item):
    display_menu()
    
    delete_item = input("Which item you want to delete: ").strip()
    
    menu_item.pop(delete_item)
    
    with open("menu.txt", "w") as file:
        for item, price in menu_item.items():
            file.write(f"{item.ljust(20)} - ${price}\n")
    
    print(f"{delete_item} has been deleted from the menu.")
    
    return menu_item