from task import Task

class TaskManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = [Task.from_dict(t) for t in self.storage.load()]

    def add_task(self, title):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title)
        self.tasks.append(task)
        self.storage.save(self.tasks)

    def list_tasks(self):
        return self.tasks

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        self.storage.save(self.tasks)

    def mark_complete(self, task_id):
        for t in self.tasks:
            if t.task_id == task_id:
                t.completed = True
        self.storage.save(self.tasks)
