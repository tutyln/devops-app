
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Gorev eklendi: {task}")

def list_tasks():
    if not tasks:
        print("Henuz gorev yok.")
        return

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

add_task("Python uygulamasini yaz")
add_task("Azure Pipeline kur")
add_task("Docker ogren")

list_tasks()
