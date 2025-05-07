

tasks=[]
def display_menu():
   print("== task manager==")
   print("1:add task")
   print("2:view task")
   print("3:complete task")
   print("4:delete task")
   print("0:exit task")

# add task 
def add_task():
    title=input("enter task title:")
    tasks.append({"title":title,"completed":False})
    print(f"Task {title} added successfully")
# view task 
def view_task():
    if not tasks:
        print("no task to display")
        return
    print(" My Task")
    for index,task in enumerate(tasks):
        status="✔" if task["completed"] else ""
        print(f" {index+1}, [{status}] {task['title']}")
    print("=======================")    
# complete task 
def complete_task():
    view_task()
    if not tasks:
        return
    try:
        task_number=int(input("enter task number to mark asda completed"))
        if task_number<1 or task_number>len(tasks):
            print("invalid number")
            return
        task_to_completed=tasks[task_number-1]
        task_to_completed['completed']=True
        print(f" Task '{task_to_completed["title"]}' mark as completed ")
    except ValueError:
        print("please enter a valid number")
# delte tassk 
def delete_task():
  view_task()
  if not tasks:
      return
  try:
    task_number=int(input("enter task number to delete"))
    if task_number<1 or task_number>len(tasks):
     print("invakid task number ")
     return
    deleted_task=tasks.pop(task_number-1)
    print(f"task '{deleted_task["title"]}' deleted successfully")
  except ValueError:
      print("enter a valid number ")  

def main():
    while True:
        display_menu()
        choice=input("enter you choice(0-4):")
        if choice=="1":
            add_task()
        elif choice=="2":
            view_task()
        elif choice=="3":
            complete_task()
        elif choice=="4":
            delete_task()
        elif  choice=="0":
            print("goodbye! 👍")
        else:
            print("invalid choice.go with 0-4 ❌")           

main()       