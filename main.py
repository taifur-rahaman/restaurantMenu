
import functionalities as func

print("Welcome to the Restaurant Menu Manangment System!")

menu_item = {}

with open("menu.txt", "r") as file:
    for line in file:
        item, price = line.split(" - $")
        menu_item[item.strip()] = price

while True:
    print("\nPlease Seletect an Option: \n1. Add Menu Item\n2. Display Menu\n3. Update Menu\n4. Delete Menu Item\n0. Exit")
    
    choice = input("\nEnter your choice: ")
    
    match choice:
        case "1":
            menu_item = func.add_item(menu_item)
        case "2":
            func.display_menu()
        case "3":
            func.update_menu(menu_item)
        case "4":
            menu_item = func.delete_item(menu_item)
        case "0":
            print("Exiting the System. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")
