import random
from menu import MenuItem
from employee import Employee
from customer import Customer
from order import Order
from restaurant import Restaurant

# Example usage with provided restaurants and menu items:
restaurants = [
    ("Branches Grill and Café – Chatham", 20),
    ("Alvah Stone, Montague", 15),
    ("Mill on the Floss, New Ashford", 10),
    ("Belfry Inn & Bistro, Sandwich, Cape Cod", 25),
    ("Mamma Maria – North Square, Boston", 30),
    ("Hope & Olive, Greenfield", 12),
    ("Sorrelina, Boston", 18),
    ("Skipper Chowder House, South Yarmouth", 22),
    ("Sarma, Boston", 16),
    ("The Blue Ox, Lynn", 14),
    ("Table, Boston", 20),
    ("K Restaurant – Peabody", 10)
]

menu_items = {
    "Branches Grill and Café – Chatham": [
        MenuItem("Jerk Wings", "Spicy Jamaican-style wings", 12.99),
        MenuItem("Fish Taco", "Fresh fish with a tangy slaw", 14.99)
    ],
    "Alvah Stone, Montague": [
        MenuItem("Farm Salad", "Seasonal greens with a light vinaigrette", 10.99),
        MenuItem("Grilled Chicken", "Marinated chicken with roasted vegetables", 18.99)
    ],
    "Mill on the Floss, New Ashford": [
        MenuItem("Roast Duckling", "Tender duck with a rich sauce", 24.99),
        MenuItem("Tournedos Bearnaise", "Filet mignon with bearnaise sauce", 29.99)
    ],
    "Belfry Inn & Bistro, Sandwich, Cape Cod": [
        MenuItem("Lamb Loin Wellington", "Lamb wrapped in pastry with a savory filling", 27.99),
        MenuItem("BBQ Salmon", "Salmon with a Mongolian BBQ glaze", 22.99)
    ],
    "Mamma Maria – North Square, Boston": [
        MenuItem("Osso Buco", "Braised veal shanks with vegetables", 26.99),
        MenuItem("Seafood Trio", "A selection of fresh seafood", 28.99)
    ],
    "Hope & Olive, Greenfield": [
        MenuItem("Brussels Sprouts", "Five-spice roasted Brussels sprouts", 9.99),
        MenuItem("Maple Butter Scallops", "Scallops with a maple butter glaze", 21.99)
    ],
    "Sorrelina, Boston": [
        MenuItem("Potato Dumplings", "Dumplings with a rich sauce", 15.99),
        MenuItem("Lobster Fettuccine", "Fettuccine with lobster and truffle butter", 32.99)
    ],
    "Skipper Chowder House, South Yarmouth": [
        MenuItem("Lobster Roll", "Fresh lobster in a toasted roll", 19.99),
        MenuItem("Fried Calamari", "Crispy fried calamari with dipping sauce", 13.99)
    ],
    "Sarma, Boston": [
        MenuItem("Meze Platter", "A selection of Mediterranean small plates", 16.99),
        MenuItem("Vegetarian Delight", "A variety of plant-based dishes", 14.99)
    ],
    "The Blue Ox, Lynn": [
        MenuItem("Burger", "Award-winning beef burger", 14.99),
        MenuItem("Modern American Dish", "A contemporary twist on a classic", 18.99)
    ],
    "Table, Boston": [
        MenuItem("Grilled Octopus", "Octopus with roasted shallots", 17.99),
        MenuItem("Artichoke Risotto", "Risotto with artichoke and mascarpone", 16.99)
    ],
    "K Restaurant – Peabody": [
        MenuItem("Korean BBQ", "Grilled Korean-style BBQ", 20.99),
        MenuItem("Bibimbap", "Mixed rice with vegetables and meat", 15.99)
    ]
}

# Create restaurants and add menu items
restaurant_objects = []
for name, tables in restaurants:
    restaurant = Restaurant(name, tables)
    for item in menu_items[name]:
        restaurant.menu.add_item(item)
    restaurant.add_employee(Employee("John Lee", "Chef"))
    restaurant.add_employee(Employee("Jane Doe", "Waiter", assigned_tables=[1, 2, 3]))
    customer = Customer("Jane Smith")
    order = Order(customer, table_number=1)
    order.add_item(menu_items[name][0])  # Add the first menu item to the order
    order.add_item(menu_items[name][1]) 
    restaurant.add_order(order)
    restaurant_objects.append(restaurant)

# Randomly select and print details of one restaurant
selected_restaurant = random.choice(restaurant_objects)
print(selected_restaurant.describe())
