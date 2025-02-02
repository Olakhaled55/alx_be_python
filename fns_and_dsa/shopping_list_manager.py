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

        # Validate that the user input is a number and within the valid range
        choice = input("Enter your choice (1-4): ")
        
        if choice.isdigit():  # Check if the input is a number
            choice = int(choice)  # Convert the input to an integer
            
            if choice == 1:
                # Prompt the user to add an item with the corrected input message
                item = input("Enter the item to add: ")  # Corrected prompt message
                shopping_list.append(item)  # Add the item to the list
                print(f"'{item}' has been added to your shopping list.")
            
            elif choice == 2:
                # Prompt the user to remove an item
                item = input("Enter the item you want to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)  # Remove the item from the list
                    print(f"'{item}' has been removed from your shopping list.")
                else:
                    print(f"'{item}' is not in your shopping list.")
            
            elif choice == 3:
                # Display the current shopping list
                if shopping_list:
                    print("Your shopping list:")
                    for index, item in enumerate(shopping_list, start=1):
                        print(f"{index}. {item}")
                else:
                    print("Your shopping list is empty.")
            
            elif choice == 4:
                # Exit the program
                print("Goodbye!")
                break
            
            else:
                # If the choice is not between 1-4
                print("Invalid choice. Please enter a number between 1 and 4.")
        
        else:
            # If the input is not a number
            print("Invalid input. Please enter a valid number between 1 and 4.")

if __name__ == "__main__":
    main()

