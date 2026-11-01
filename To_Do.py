def task(): #create function
    tasks=[]#
    print("----Welcome to the task management----")

    #take input from users and how many task you what to add

    total_task=int(input("How many task you want to add =")) #5
    for i in range(1, total_task+1):
        task_name=input(f"Enter task{i} =")
        tasks.append(task_name) #end the task will add

    print(f"Todays tasks are\n {tasks}")

    while True:
        operation=int(input("\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n Select Number from above operations = "))

        if operation==1:
            add=input("Enter task u want to add = ")
            tasks.append(add)
            print(f"Task{add} has been successfully added...")

        elif operation==2:
            update_val= input("Enter the task name you want to update =")
            if update_val in tasks:
                up=input("Enter new task")
                ind = tasks.index(update_val)
                tasks[ind]=up
                print(f"Updated task {up}")

        elif operation==3:
            del_val=input("which task u want to delete = ")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f"Tasks {del_val} has been deleted....")
        elif operation==4:
            print(f"Total tasks = {tasks}")

        elif operation==5:
            print("Closing the program...")
            break

        else:
            print("INVALID Input")



task()

