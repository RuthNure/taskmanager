# Main.py
from TaskFunctions import *


def startsystem():
    # Initialization code for the College Task Tracker system
    # You can set up any required data structures or configurations here
    print("College Task Tracker System")


def userinput():
    while True:
        assignment = input("Enter the assignment (or 'done' to finish): ")

        if assignment.lower() == 'done':
            return None

        while True:
            deadline = input("Enter the deadline (e.g., YYYY-MM-DD): ")

            if validate_date(deadline):
                break
            else:
                print("Invalid date format. Please enter the date in the correct format (YYYY-MM-DD).")

        priority_level = int(input("Enter the priority level (1 being top priority, 3 being bottom priority): "))
        return assignment, deadline, priority_level
    
def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def feature(feature_number, tasks):
    # Execute the specified feature based on the user's input
    # Call the relevant functions from TaskFunctions.py
    if feature_number == '1':
        user_input = userinput()
        if user_input is not None:
            assignment, deadline, priority_level = user_input
            addtask(assignment, deadline, priority_level, tasks)
            print("Task added successfully!")

    elif feature_number == '2':
        displaytasks(tasks)

    elif feature_number == '3':
        task_id = int(input("Enter task ID to pull: "))
        get_task_by_id(task_id, tasks)

    elif feature_number == '0':
        print("Exiting College Task Tracker System.")
        return False

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 0.")

    return True


if __name__ == "__main__":
    startsystem()

    tasks = []

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Display All Tasks")
        print("3. Enter task ID")
        print("0. Exit")

        choice = input("Enter your choice (0-3): ")

        if not feature(choice, tasks):
            break
