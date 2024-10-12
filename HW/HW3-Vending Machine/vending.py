from product import Product

class VendingMachine:
    """Initialisate Vending mashine """
    def __init__(self):
           self.inventory = {}
           self.total_sales = 0.0

    def print_inventory(self):
           for location, details in self.inventory.items():
             
             product_names = [product.product_name for product in details["products"]]
             print(f"Slot {location}: {product_names} at ${details['unit_price']} each")

    def stock_item(self, location, product_list, unit_price):
            
            self.inventory[location] = {"products": product_list,"unit_price": unit_price}

    def purchase(self, location, money):
        if location not in self.inventory or not self.inventory[location]["products"]:
                 return Product("Empty Product"), money

        unit_price = self.inventory[location]["unit_price"]

        if money < unit_price:
              return Product("Empty Product"), money

        product = self.inventory[location]["products"].pop(0)
        change = money - unit_price

        self.total_sales += unit_price

        return product, change
