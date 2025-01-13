def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize the shopping list as an empty list

    while True:
        display_menu()  # Show the menu options
        choice = input("Enter your choice: ")  # Get user input for menu selection

        if choice == '1':
            # Prompt the user to add an item
            item = input("Enter the item you want to add: ")
            shopping_list.append(item)  # Add the item to the list
            print(f"'{item}' has been added to your shopping list.")
        
        elif choice == '2':
            # Prompt the user to remove an item
            item = input("Enter the item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item from the list
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")
        
        elif choice == '3':
            # Display the current shopping list
            if shopping_list:
                print("Your shopping list:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
