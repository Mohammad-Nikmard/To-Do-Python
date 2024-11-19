class ToDoManager:
    def __init__(self):
        self.tasks = [] 
        
    def add_task(self, task):
        """Adds a task to the to-do list."""
        self.tasks.append({"name": task, "completed": False})
        print(f"Task added: {task}")



