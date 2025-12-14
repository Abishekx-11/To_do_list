
# we will be handling everything through list and file
Task = []       # creates empty list

def load_task():
    try:
        with open("app.txt", "r", encoding="utf-8") as file:      # open file to read, encoding="utf-8" -> support every language,symbols,characters, emojis
            for content in file:
                Task.append(content.strip())
            
    except FileNotFoundError:
        pass                                           # if file not found, it silently handle 

def save_task():
    with open("app.txt","w", encoding="utf-8") as file:     # open file to write, if file already exist, it overwrite contents in that file
        for content in Task: 
            file.write(content+"\n")
        


def add_task():
    input_task = input("Enter the task: ")
    if input_task == "":                        # handles empty input from user
        print("First enter some task !")
    else:
        Task.append("[ ] "+ input_task)
        print("Task Added Successfully !")
        save_task()


def show_task():
    if len(Task) == 0:
       print("No task added yet !")
            
    else:
        for i , task_name in enumerate(Task, 1):   # show task with bullet numbers
            print(f"{i}. {task_name}")



def delete_task():
    if len(Task) == 0:    # if no task in list, simply return
        print("No Task added yet !")
        return
    else:
        show_task()
        try:
            user_input = int(input("Enter task number you want to delete: "))
            if 1 <= user_input <= len(Task):        #checks if user_input as index is valid or not to perfrom 
                text = Task.pop(user_input - 1)
                save_task()
                print("Deleted Task: " + text)
            else:
                print("This Task number is not available\n\n")
            
        except ValueError:
            print("Enter number only !")

    


def mark_complete():
    if len(Task) == 0:              # if no task in list, simply return 
        print("No Task added yet !")
        return
    else:
        show_task()
        try:
            user_input = int(input("Enter task number you want to mark as completed: "))
            if 1 <= user_input <= len(Task):            #checks if user_input as index is valid or not to perfrom 
                current_task = Task[user_input - 1]

                if "[✓]" in current_task:
                    print("Task already completed")

                else:
                    Task[user_input - 1] = current_task.replace("[ ]", "[✓]")         #replace and assign it =s value to same index, simply updating
                    save_task()
                    print("Task Marked as completed")

            else:
                print("This task number is not available\n\n")
        except ValueError:
            print("Enter number only !")




def main():
    load_task()     # if loads content from file to list

    print("--OPTIONS__")
    print("1.Add Task\n2.Delete Task\n3.Show Task\n4.Mark Complete\n5.Show Options\n6.Exit")
    while True:
        try:
            user = int(input("--> Enter Task that you want to perform: "))
        except ValueError:
            print("Enter number only !")
            continue

        if (user == 1):
            add_task()
        elif (user == 2):
            delete_task()
        elif (user == 3):
            show_task()
        elif (user == 4):
            mark_complete()
        elif(user == 5):
            print("1.Add Task\n2.Delete Task\n3.Show Task\n4.Mark Complete\n5.Show Options\n6.Exit")
        elif (user == 6):
            print("Exiting Program")
            break
        else:
            print("Invalid Input !")
        


main()




