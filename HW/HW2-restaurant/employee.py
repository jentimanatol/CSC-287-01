class Employee:
    """Represents an employee of the restaurant."""
    def __init__(self, name, position, assigned_tables=None):
        self.name = name
        self.position = position
        self.assigned_tables = assigned_tables if assigned_tables is not None else []

    def describe(self):
        tables = ', '.join(map(str, self.assigned_tables))
        return f"{self.name}, {self.position}, Assigned Tables: {tables}"
