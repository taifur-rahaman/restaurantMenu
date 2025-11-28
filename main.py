
import functionalities as func

print("Welcome to the Restaurant Menu Manangment System!")

while True:
    print("\nPlease Seletect an Option: \n1. Add Menu Item\n2. Display Menu\n4. Delete Menu Item\n0. Exit")
    
    choice = input("\nEnter your choice: ")
    
    match choice:
        case "1":
            func.add_item()
        case "2":
            func.display_menu()
        case "4":
            pass
        case "0":
            print("Exiting the System. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")
