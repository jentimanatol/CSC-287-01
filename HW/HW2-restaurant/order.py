class Order:
    """Represents an order placed by a customer."""
    def __init__(self, customer, table_number):
        self.customer = customer
        self.table_number = table_number
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_bill(self):
        return sum(item.price for item in self.items)

    def describe(self):
        description = f"Order for {self.customer.describe()} at Table {self.table_number}:\n"
        for item in self.items:
            description += item.describe() + "\n"
        description += f"Total Bill: ${self.total_bill():.2f}"
        return description
