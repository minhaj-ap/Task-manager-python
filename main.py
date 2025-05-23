import json
from datetime import datetime
import os

FILE_NAME = "task.json"  # file name goes here


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


def displayData(task_list: list, showId=False):
    listN = sorted(
        task_list,
        key=lambda x: datetime.strptime(x["deadline"], "%Y-%m-%d"),
    )
    for i in range(len(listN)):
        id_part = f"ID: {listN[i]['id']}\t" if showId else ""
        print(
            f"{id_part}Title:{listN[i]['title']}\tDeadline:{listN[i]['deadline']}\tPriority:{listN[i]['priority']}\tCompleted:{listN[i]['completed']}"
        )
    print("\n")


def loadTask() -> list:
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


def addTask():
    print("Add new task")
    title = input("Enter title: ")
    while True:
        try:
            deadline = input("Enter deadline in the format YYYY-MM-DD: ")
            datetime.strptime(deadline, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid format")
    priority = input("Enter H for high priority and L for low priority: ").upper()
    id = DATA[-1]["id"] + 1
    print(f"Recieved data:{title},{deadline},{priority},{id}")
    recievedData = {
        "id": id,
        "title": title,
        "deadline": deadline,
        "priority": "High" if priority == "H" else "Low",
        "completed": False,
    }
    DATA.append(recievedData)
    with open(FILE_NAME, "w") as file:
        json.dump(DATA, file, indent=4)


def editTask():
    task = DATA
    if len(task) <= 0:
        print("NO TASKS FOR EDIT")
        return
    print("HERE ARE THE TASKS YOU CAN EDIT\n")
    displayData(task, True)
    try:
        id = int(input("Enter the id to be edited: "))
    except ValueError:
        print("Only numbers are allowed")
        id = int(input("Enter the id to be edited: "))
    selected_task = [e for e in task if e["id"] == id]
    new_data = {}
    for key, obj in selected_task[0].items():
        new_data[key] = obj
    for key, obj in selected_task[0].items():
        if key == "id" or key == "completed":
            continue
        if key == "deadline":
            while True:
                new_value = input(
                    f"Enter DEADLINE, leave empty for no change (currently: {obj}) (format:YYYY-MM-DD): "
                )
                if new_value == "":
                    break
                try:
                    datetime.strptime(new_value, "%Y-%m-%d")
                    new_data[key] = new_value
                    break
                except ValueError:
                    print("Invlaid format")
            continue
        if key == "priority":
            while True:
                try:
                    new_value = input(
                        f"Enter priority , H for high and L for low, leave empty for no changes (currently:{obj}): "
                    ).upper()
                    if new_value == "":
                        break
                    if new_value != "":
                        if new_value == "H":
                            new_data["priority"] = "High"
                            break
                        elif new_value == "L":
                            new_data["priority"] = "Low"
                            break
                        else:
                            raise ValueError()
                except ValueError:
                    print("Only H and L are valid inputs")
            continue
        new_value = input(
            f"Enter {(key).upper()} ,leave empty for no change (currently: {obj}): "
        )
        if new_value != "":
            new_data[key] = new_value

    for e in DATA:
        if e["id"] == id:
            e.update(new_data)
    with open(FILE_NAME, "w") as file:
        json.dump(DATA, file, indent=4)
    print("Successfully updated")


def markComplete():
    global DATA
    tasks = DATA
    if len(DATA) <= 0:
        print("Seems like file is empty")
        return
    viewPendingTask(True)
    try:
        id_to_mark = int(input("Enter the id to mark complete: "))
    except ValueError:
        print("only numbers are allowed")
        id_to_mark = int(input("Enter the id to mark complete: "))
    for task in DATA:
        if task["id"] == id_to_mark:
            task["completed"] = True
    with open(FILE_NAME, "w") as file:
        json.dump(DATA, file, indent=4)
    print("Successfully updated!!")


def deleteTask():
    global DATA
    tasks = DATA
    if len(DATA) <= 0:
        print("Seems like file is empty")
        return
    print("\nHERE ARE YOUR TASKS SORTED ON THE BASIS OF DEADLINE\n")
    displayData(tasks, True)
    try:
        id_to_dlt = int(input("Enter the id to delete: "))
    except ValueError:
        print("only numbers are allowed")
        id_to_dlt = int(input("Enter the id to delete: "))
    DATA = [e for e in DATA if e["id"] != id_to_dlt]
    with open(FILE_NAME, "w") as file:
        json.dump(DATA, file, indent=4)
    print("Successfully deleted!!")


def viewTask():
    tasks = DATA
    if len(DATA) <= 0:
        print("Seems like file is empty")
        return
    print("\nHERE ARE YOUR TASKS SORTED BY DEADLINE\n")
    displayData(tasks)


def viewPendingTask(showId=False):
    if len(DATA) <= 0:
        print("No tasks found")
        return
    pTask = [e for e in DATA if not e["completed"]]
    if len(pTask) <= 0:
        print("Everything is completed")
        return
    print("\nHERE ARE YOUR PENDING TASKS SORTED BY DEADLINE\n")
    displayData(pTask, showId=showId)


def sortedData():
    if (len(DATA)) <= 0:
        print("File looks empty")
        return
    sortedList = sorted(DATA, key=lambda x: x["priority"] != "High")
    # The ones with priority high will retrun 0 and therefore first
    print("\nHERE IS THE SORTED DATA\n")
    displayData(sortedList)


def main():
    print("Welcome to task manager")
    print("To view tasks input 1")
    print("To edit tasks input 2")
    print("To add tasks input 3")
    print("To delete tasks input 4")
    print("To mark complete a  task input 5")
    print("To view pending tasks input 6")
    print("To view tasks sorted by priority input 7\n")
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
        elif choice == 7:
            sortedData()
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
