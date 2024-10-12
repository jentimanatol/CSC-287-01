
"""Our vending machine will have an unlimited number of slots.  A slot has a location, for example “A1”, and it will contain N products of the same type.  For example, “A1” may contain 10 diet cokes.

Your vending machine must support the following operations:

stock_item(): with three parameters
location: a slot location, e.g., “A1”
product_list, a list of product objects, e.g. 2 Diet Coke Objects.
unit_price: unit price for this slot, e.g. 1.50.

print_inventory(): prints out all the slots with product details.  Sample output provided below.

purchase(): with two parameters:
location: a slot location, e.g. “A1”
money: amount of money the user deposits, e.g. 2.0
purchase will then return a tuple with two parts:
product: for example, if the user selects “A1”, they will get back a Diet Coke Object.  If there are no more Diet Cokes or the user does not provide enough money, you should return a Product object with the name set to “Empty Product”
change: for example, if a user deposits $2 and a Diet Coke costs $1.50, the user will receive .50 in change.

You will also need to model a Product Class, a Drink Class and a Snack Class.  Each of these should support a single method:

consume():
For the Drink Class, you can output: f”"Yum, you drink the {self.product_name}."
For the Snack Class, you can output:  f“Yum, you eat the {self.product_name}”.
For the Product Class, you can output “Sorry, this product is empty”

Here is my sample code to get your started:
 """
from vending import VendingMachine
from product import Drink
from product import Snack

# Create a vending machine
vending_machine = VendingMachine()

# Create 3 Diet Cokes
diet_coke_list = []
for i in range(3):
    diet_coke = Drink("Diet Coke")
    diet_coke_list.append(diet_coke)

# Create 2 Cliff Bars
cliff_bar_list = []
for i in range(2):
    cliff_bar = Snack("Cliff Bar")
    cliff_bar_list.append(cliff_bar)

# Stock the vending machine with various products
vending_machine.stock_item("A1", diet_coke_list, 1.50)
vending_machine.stock_item("B1", cliff_bar_list, 3.25)

# Print the inventory
vending_machine.print_inventory()

print("> Attempt to buy diet coke with $2.00")
(product, change) = vending_machine.purchase("A1", 2.0)
print(f"You just got:  {product.product_name}")
print(f"Your change:  {change}")
print(f"Total machine sales:  {vending_machine.total_sales}")
product.consume()

print("> Attempt to buy diet coke with $1.00")
(product, change) = vending_machine.purchase("A1", 1.0)
print(f"You just got:  {product.product_name}")
print(f"Your change:  {change}")
print(f"Total machine sales:  {vending_machine.total_sales}")
product.consume()

print("> Attempt to buy Cliff Bar with $10.00")
(product, change) = vending_machine.purchase("B1", 10.0)
print(f"You just got:  {product.product_name}")
print(f"Your change:  {change}")
print(f"Total machine sales:  {vending_machine.total_sales}")
product.consume()


#And, here is my sample output:
