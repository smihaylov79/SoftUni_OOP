from project.task import Task
class Section:
    def __init__(self, name):
        self.name = name
        self.tasks=[]

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        try:
            task=[el for el in self.tasks if el.name==task_name][0]
            task.completed=True
            return f"Completed task {task_name}"
        except IndexError:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks=[el for el in self.tasks if el.completed]
        not_completed=[el for el in self.tasks if not el.completed]
        self.tasks=not_completed
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        result=f"Section {self.name}:\n"
        result+=f"\n".join([el.details() for el in self.tasks])
        return result