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


def displayData(list: list):
    print(
        f"Title:{list[0]['title']}\tDeadline:{list[0]['deadline']}\tPriority:{list[0]['priority']}\tCompleted:{list[0]['completed']}"
    )


def addTask():
    print("Add task")


def editTask():
    print("Edit task")


def markComplete():
    print("mark complete")


def deleteTask():
    print("Delete task")


def loadTask():
    global DATA
    if os.path.exists(FILE_NAME):
        if os.path.getsize(FILE_NAME) == 0:
            print("No tasks exists in the file")
            DATA = []
            return
        try:
            with open(FILE_NAME, "r") as file:
                DATA = json.load(file)
        except json.JSONDecodeError:
            print("Error: task.json is not a valid JSON file.")
            DATA = []
            return
    else:
        print("Please add a task.json file in the folder")
        return


def viewTask():
    tasks = DATA
    if len(DATA) <= 0:
        print("Seems like file is empty")
        return
    displayData(tasks)


def viewPendingTask():
    if len(DATA) <= 0:
        print("No tasks found")
        return
    pTask = [e for e in DATA if not e["completed"]]
    if len(pTask) <= 0:
        print("Everything is completed")
        return
    displayData(pTask)


def sortedData():
    print("sorted data")


def main():
    print("Welcome to task manager")
    print("To view tasks input 1")
    print("To edit tasks input 2")
    print("To add tasks input 3")
    print("To delete tasks input 4")
    print("To mark complete a  task input 5")
    print("To view pending tasks input 6")
    print("To view tasks sorted by priority input 7")
    loadTask()
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
        elif choice==7:
            sortedData()
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
