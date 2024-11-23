class MenuItem:
    """Represents an item on the menu."""
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def describe(self):
        return f"{self.name}: {self.description} - ${self.price:.2f}"

class Menu:
    """Represents the menu of the restaurant."""
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def describe(self):
        description = "Menu:\n"
        for item in self.items:
            description += item.describe() + "\n"
        return description
