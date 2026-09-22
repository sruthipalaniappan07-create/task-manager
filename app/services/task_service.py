from app.repositories.task_repository import TaskRepository


class TaskService:

    def __init__(self, repository=None):
        self.repository = repository or TaskRepository()

    def create_task(self, title, description=""):
        if not title or not title.strip():
            raise ValueError("Task title is required")

        return self.repository.create_task(
            title.strip(),
            description.strip()
        )

    def get_all_tasks(self):
        return self.repository.get_all_tasks()

    def get_task(self, task_id):
        if task_id <= 0:
            raise ValueError("Invalid task ID")

        return self.repository.get_task_by_id(task_id)

    def update_task(self, task_id, title, description, completed):
        if task_id <= 0:
            raise ValueError("Invalid task ID")

        if not title or not title.strip():
            raise ValueError("Task title is required")

        if len(title.strip()) < 3:
             raise ValueError("Task title must contain at least 3 characters")

        return self.repository.update_task(
            task_id,
            title.strip(),
            description.strip(),
            completed
        )

    def delete_task(self, task_id):
        if task_id <= 0:
            raise ValueError("Invalid task ID")

        return self.repository.delete_task(task_id)
