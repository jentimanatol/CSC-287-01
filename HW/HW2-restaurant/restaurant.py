from menu import Menu
from employee import Employee
from order import Order

class Restaurant:
    """Represents the restaurant itself."""
    def __init__(self, name, number_of_tables):
        self.name = name
        self.menu = Menu()
        self.employees = []
        self.orders = []
        self.number_of_tables = number_of_tables
        self.available_tables = number_of_tables

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_order(self, order):
        if self.available_tables > 0:
            self.orders.append(order)
            self.available_tables -= 1
        else:
            print(f"No available tables at {self.name}")

    def describe(self):
        description = f"Restaurant: {self.name}\n"
        description += f"Available Tables: {self.available_tables}/{self.number_of_tables}\n"
        description += self.menu.describe() + "\n"
        description += "Employees:\n"
        for employee in self.employees:
            description += employee.describe() + "\n"
        description += "Orders:\n"
        for order in self.orders:
            description += order.describe() + "\n"
        return description
