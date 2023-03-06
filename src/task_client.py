class Task:
    def __init__(self, project: str, priority: int = 1):
        self.project = project
        self.priority = priority
        self.assigned_to_resource = False

    def __repr__(self) -> str:
        return self.project