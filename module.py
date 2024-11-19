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

    def delete_task(self, index):
        """Deletes a task by its index."""
        if 0 < index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Task removed: {removed_task['name']}")
        else:
            print("Invalid task number.")

    def delete_all_tasks(self):
        """Deletes all tasks from the to-do list."""
        if self.tasks:
            self.tasks.clear()
            print("All tasks have been deleted.")
        else:
            print("No tasks to delete.")

    def mark_task_as_complete(self, index):
        """Marks a task as complete by its index."""
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
            print(f"Task marked as complete: {self.tasks[index - 1]['name']}")
        else:
            print("Invalid task number.")


    def search_task(self, keyword):
        """Searches for tasks containing the given keyword."""
        found_tasks = [
            f"{i}. {task['name']}" for i, task in enumerate(self.tasks, 1) if keyword.lower() in task["name"].lower()
        ]
        if found_tasks:
            print("Search Results:")
            for task in found_tasks:
                print(task)
        else:
            print(f"No tasks found containing '{keyword
