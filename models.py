class Task:
    def __init__(self, id, title, description, is_completed, created_at, updated_at = None):
        self.id = id
        self.title = title
        self.description = description
        self.is_completed = is_completed
        self.created_at = created_at
        self.updated_at = updated_at