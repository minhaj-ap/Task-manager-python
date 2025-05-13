def addTask():
    print("Add task")
def editTask():
    print("Edit task")
def markComplete():
    print("mark complete")
def deleteTask():
    print("Delete task")
def viewTask():
    print("view task")
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
        choice=int(input("Enter your choice: "))
        if choice==1:
            viewTask()
        elif choice==2:
            editTask()
        elif choice==3:
            addTask()
        elif choice==4:
            deleteTask()
        elif choice==5:
            markComplete()
        elif choice==6:
            viewPendingTask()
        else:
            print("Invalid input")
            
if __name__ == "__main__":
    main()