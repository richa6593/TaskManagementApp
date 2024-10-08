print("...........Welcome to TASK MANAGEMENT APP............\n")
tasks=[]
total_task=int(input("Enter how many tasks you want to add :"))
for i in range(1,total_task+1):
    task_name=input(f"Enter your {i} task :")
    tasks.append(task_name)
print(f"Today's tasks are:\n{tasks}\n")


while True:
    operations = int(input("Enter 1-Add\n 2-Update\n 3-Delete\n 4-View\n 5-Exit\Stop\n"))
    if operations==1:
        add=input("Enter task you want to add :")
        tasks.append(add)
        print(f"\nThe task {add} has been added successfully.")

    elif operations==2:
        modify_val=input("Enter task you want to update :")
        if modify_val in tasks:
            up=input("Enter new task : ")
            ind=tasks.index(modify_val)
            tasks[ind]=up
        print(f"\nThe task {up} has been updated successfully.")

    elif operations==3:
        del_val=input("Enter task you want to delete :")
        if del_val in tasks:
            ind=tasks.index(del_val)
        tasks.remove(del_val)
        print(f"\nThe task {del_val} has been deleted successfully.")

    elif operations==4:
        print(f"The list of tasks are {tasks}")
        
    elif operations==5:
        print("Closing the task")
        break
    else:
        print("Invalid input")


