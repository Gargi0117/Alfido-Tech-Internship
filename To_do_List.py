def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add To-Do Item")
    print("3. Remove To-Do Item")
    print("4. Exit")

def view_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for idx, item in enumerate(todo_list, start=1):
            print(f"{idx}. {item}")

def add_todo_item(todo_list):
    item = input("Enter the to-do item: ").strip()
    if item:
        todo_list.append(item)
        print(f"Added: '{item}'")
    else:
        print("Cannot add an empty item.")

def remove_todo_item(todo_list):
    if not todo_list:
        print("Your to-do list is empty. Nothing to remove.")
        return
    view_todo_list(todo_list)
    try:
        index = int(input("Enter the number of the item to remove: "))
        if 1 <= index <= len(todo_list):
            removed = todo_list.pop(index - 1)
            print(f"Removed: '{removed}'")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter a valid number.")

def todo_app():
    todo_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_todo_item(todo_list)
        elif choice == '3':
            remove_todo_item(todo_list)
        elif choice == '4':
            print("Exiting To-Do List app. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    todo_app()
