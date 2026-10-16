
tasks = []

def add_task(task):
    tasks.append(task)
    return task

def list_tasks():
    return tasks

if __name__ == "__main__":
    add_task("Python uygulamasini yaz")
    add_task("Azure Pipeline kur")
    add_task("Docker ogren")

    for number, task in enumerate(list_tasks(), start=1):
        print(f"{number}. {task}")
