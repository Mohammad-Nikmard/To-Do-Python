from module import ToDoManager
from utils import print_menu, get_user_input
from constants import WELCOME_MESSAGE, INVALID_CHOICE

def main():
    print(WELCOME_MESSAGE)
    todo_manager = ToDoManager()

    while True:
        print_menu()
        choice = get_user_input("Enter your choice: ")

        if choice == "1":
            task = get_user_input("Enter the task to add: ")
            todo_manager.add_task(task)
        elif choice == "2":
            todo_manager.view_tasks()
        elif choice == "3":
            index = get_user_input("Enter the task number to delete: ")
            try:
                todo_manager.delete_task(int(index))
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            todo_manager.delete_all_tasks()
        elif choice == "5":
            index = get_user_input("Enter the task number to mark as complete: ")
            try:
                todo_manager.mark_task_as_complete(int(index))
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "6":
            keyword = get_user_input("Enter a keyword to search for tasks: ")
            todo_manager.search_task(keyword)
        elif choice == "7":
            print("Exiting. Goodbye!")
            break
        else:
            print(INVALID_CHOICE)

if __name__ == "__main__":
    main()

