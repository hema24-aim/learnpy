from task_manager import TaskManager
from storage import Storage
from logger import log_action

def main():
    tm = TaskManager(Storage())

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Complete Task\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Task title: ")
            tm.add_task(title)
            log_action(f"Added task: {title}")

        elif choice == "2":
            for t in tm.list_tasks():
                print(f"{t.task_id} - {t.title} [{'✔' if t.completed else '❌'}]")

        elif choice == "3":
            task_id = int(input("Enter task id: "))
            tm.delete_task(task_id)
            log_action(f"Deleted task {task_id}")

        elif choice == "4":
            task_id = int(input("Enter task id: "))
            tm.mark_complete(task_id)
            log_action(f"Completed task {task_id}")

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
