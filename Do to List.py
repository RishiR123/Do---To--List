Tasks = []

# Developer Name
developer_name = "Rishi R"

# Functions

def add():
    global Tasks  # Declare to modify the global variable
    adding = input("Enter the Task you want to add to the list: ")
    Tasks.append(adding)
    print(f"Your Task: {adding} is added to the list successfully ")
    view = input("Want to see the whole list? (yes or no): ")
    if view.lower() == "yes":
        show()

def delete():
    global Tasks  # Declare to modify the global variable
    print("Listing the whole List!")
    print(Tasks)
    deleting = input("Enter the # of the Task you want to delete: ")
    try:
        deleting = int(deleting)
        if deleting < len(Tasks):
            print(f"Your Task: {Tasks[deleting]} deleted")
            Tasks.pop(deleting)
        else:
            print("The specified task is not there in the list. Enter the right task #")
    except ValueError:
        print("Please enter a valid integer.")

def show():
    print("Here is the list of your tasks to be done")
    for index, task in enumerate(Tasks):
        print(index, ".", task)

if __name__ == "__main__":
    # Credits
    print("To-Do List App")
    print("Developed by:", developer_name)
    print("---------------------")
    while True:
        # Interface
        print("Welcome to Do-To-List")
        print("---------------------")
        print("Operations:\n")
        print("1. Add a new Task")
        print("2. Delete a Task")
        print("3. List the Tasks")
        print("4. Quit")

        choice = int(input("Pick the operation to be done: "))

        if choice == 1:
            add()
        elif choice == 2:
            delete()
        elif choice == 3:
            show()
        elif choice == 4:
            break

    print("Goodbye")
