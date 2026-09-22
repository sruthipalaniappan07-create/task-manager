class Task:
    def __init__(
        self,
        task_id=None,
        title="",
        description="",
        completed=False
    ):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
