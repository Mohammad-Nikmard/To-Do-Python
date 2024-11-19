class ToDoManager:
    def __init__(self):
        self.tasks = [] 
        
    def add_task(self, task):
        """Adds a task to the to-do list."""
        self.tasks.append({"name": task, "completed": False})
        print(f"Task added: {task}")


    def view_tasks(self):
        """Displays all tasks in the to-do list."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = "[X]" if task["completed"] else "[ ]"
                print(f"{i}. {status} {task['name']}")


