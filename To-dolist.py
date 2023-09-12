tasks=[]
def add_task():
    task=input("enter a task:")
    tasks.append(task)
    print("task added successfully!")
def view_tasks():
    if len(tasks)==0:
        print("no tasks found!")
    else:
        print("tasks:")
        for i,task in enumerate(tasks):
            print(f"{i+1}.{task}")
def update_task():
    view_tasks()
    task_index=int(input("enter the task number to update:"))-1
    if task_index<0 or task_index>len(tasks):
        print("invalid task number!")
    else:
        new_task=input("enter the new task:")
        tasks[task_index]=new_task
        print("task update successfully!")
while True:
    print("To-Do list application")
    print("1.add task")
    print("2.view tasks")
    print("3.update task")
    print("4.quit")
    choice=input("enter your choice:")

    if choice=="1":
        add_task()
    elif choice=="2":
        view_tasks()
    elif choice=="3":
        update_task()
    elif choice=="4":
        break
    else:
        print("invalid choice! please try again.")
