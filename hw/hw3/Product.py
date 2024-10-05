class Product:
    def __init__(self, product_name):
        self.product_name = product_name

    def consume(self):
        print("empty")

class Drink(Product):
    def consume(self):
        print(f"Drink: {self.product_name}")

class Snack(Product):
    def consume(self):
        print(f"Snack: {self.product_name}")
