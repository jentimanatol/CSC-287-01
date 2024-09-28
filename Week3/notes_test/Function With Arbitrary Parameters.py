
def make_pizza(size, *args):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in args:
        print(f"- {topping}")



make_pizza("16", "pepperoni", "mushrooms", "extra cheese","extra topic","test metod")
