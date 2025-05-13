import json
import datetime
import os

FILE_NAME = "task.json"


# Expected task.json format
# [
#   {
#     "id":1,
#     "title": "Finish Python project",
#     "deadline": "2025-05-13",
#     "priority": "High",
#     "completed": false
#   }
# ]
def addTask():
    print("Add task")


def editTask():
    print("Edit task")


def markComplete():
    print("mark complete")


def deleteTask():
    print("Delete task")


def viewTask():
    if os.path.exists(FILE_NAME):
        if os.path.getsize(FILE_NAME) == 0:
            print("No tasks found to be displayed \nAdd one now!")
            return
        try:
            with open(FILE_NAME, "r") as file:
                tasks = json.load(file)
            print(
                f"Title:{tasks[0]['title']}\tDeadline:{tasks[0]['deadline']}\tPriority:{tasks[0]['priority']}\tCompleted:{tasks[0]['completed']}"
            )
        except json.JSONDecodeError:
            print("Error: task.json is not a valid JSON file.")
    else:
        print("Please add a task.json file in the folder")


def viewPendingTask():
    print("view pending task")


def main():
    print("Welcome to task manager")
    print("To view tasks input 1")
    print("To edit tasks input 2")
    print("To add tasks input 3")
    print("To delete tasks input 4")
    print("To mark complete a  task input 5")
    print("To view pending tasks input 6")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            viewTask()
        elif choice == 2:
            editTask()
        elif choice == 3:
            addTask()
        elif choice == 4:
            deleteTask()
        elif choice == 5:
            markComplete()
        elif choice == 6:
            viewPendingTask()
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
