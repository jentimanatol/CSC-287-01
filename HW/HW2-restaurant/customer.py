class Customer:
    """Represents a customer of the restaurant."""
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Customer: {self.name}"
