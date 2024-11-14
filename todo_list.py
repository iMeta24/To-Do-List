# todo_list.py

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def mark_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def display_tasks():
    for i, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i + 1}. {task['task']} - {status}")

# Sample usage
add_task("Buy groceries")
add_task("Finish homework")
mark_completed(1)
display_tasks()
