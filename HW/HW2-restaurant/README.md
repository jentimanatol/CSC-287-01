
# Restaurant Management System

Welcome to the Restaurant Management System project! This project is designed to help manage various aspects of a restaurant, including menu items, employees, orders, and tables. It's a great addition to your portfolio and showcases your skills in object-oriented programming with Python.

## Overview

This project includes the following features:
- **Menu Management**: Add and describe menu items.
- **Employee Management**: Add employees and assign tables.
- **Order Management**: Create and manage customer orders.
- **Table Management**: Track the number of available tables in the restaurant.

## Features

- **Dynamic Menu**: Easily add, update, and remove menu items.
- **Employee Management**: Assign tables to waitstaff and track their responsibilities.
- **Order Processing**: Handle customer orders and calculate total bills.
- **Table Availability**: Monitor and manage the availability of tables in real-time.

## Project Structure

The project is organized into several modules, each handling a specific aspect of the restaurant management system:

- `menu.py`: Contains the `MenuItem` and `Menu` classes.
- `employee.py`: Contains the `Employee` class.
- `customer.py`: Contains the `Customer` class.
- `order.py`: Contains the `Order` class.
- `restaurant.py`: Contains the `Restaurant` class.
- `main.py`: The main script to create and manage restaurants.

## Classes and Files

### MenuItem Class
- **File**: `menu.py`
- **Description**: Represents an item on the menu.
- **Methods**:
  - `describe()`: Returns a string description of the menu item.

### Menu Class
- **File**: `menu.py`
- **Description**: Represents the menu of the restaurant.
- **Methods**:
  - `add_item(item)`: Adds a menu item to the menu.
  - `describe()`: Returns a string description of the menu.

### Employee Class
- **File**: `employee.py`
- **Description**: Represents an employee of the restaurant.
- **Methods**:
  - `describe()`: Returns a string description of the employee.

### Customer Class
- **File**: `customer.py`
- **Description**: Represents a customer of the restaurant.
- **Methods**:
  - `describe()`: Returns a string description of the customer.

### Order Class
- **File**: `order.py`
- **Description**: Represents an order placed by a customer.
- **Methods**:
  - `add_item(item)`: Adds a menu item to the order.
  - `total_bill()`: Calculates the total bill for the order.
  - `describe()`: Returns a string description of the order.

### Restaurant Class
- **File**: `restaurant.py`
- **Description**: Represents the restaurant itself.
- **Methods**:
  - `add_employee(employee)`: Adds an employee to the restaurant.
  - `add_order(order)`: Adds an order to the restaurant.
  - `describe()`: Returns a string description of the restaurant.

## How to Run the Project

To get started with this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/restaurant-management-system.git
    cd restaurant-management-system
    ```

2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

3. Run the main script:
    ```bash
    python main.py
    ```

## Detailed Explanation

This project is designed to simulate the management of a restaurant. It includes classes to represent menu items, employees, customers, orders, and the restaurant itself. Each class has methods to manage its respective data and interactions with other classes.

### Example Usage

Here's an example of how to use the Restaurant Management System:

1. **Create a Restaurant**:
    ```python
    from restaurant import Restaurant
    restaurant = Restaurant("The Blue Ox", 20)
    ```

2. **Add Menu Items**:
    ```python
    from menu import MenuItem
    restaurant.menu.add_item(MenuItem("Burger", "Award-winning beef burger", 14.99))
    ```

3. **Add Employees**:
    ```python
    from employee import Employee
    restaurant.add_employee(Employee("John Doe", "Chef"))
    ```

4. **Create and Add Orders**:
    ```python
    from customer import Customer
    from order import Order
    customer = Customer("Jane Smith")
    order = Order(customer, table_number=1)
    order.add_item(MenuItem("Burger", "Award-winning beef burger", 14.99))
    restaurant.add_order(order)
    ```

5. **Print Restaurant Details**:
    ```python
    print(restaurant.describe())
    ```

## Screenshots

Here are some screenshots of the project in action:

![Main Test Classes](https://github.com/jentimanatol/CSC-287-01/blob/main/HW/HW2-restaurant/Screenshot/MainTestClases.jpg)
![Diagram](https://github.com/jentimanatol/CSC-287-01/blob/main/HW/HW2-restaurant/Screenshot/Untitled%20Diagram.drawio.png)

## Contributing

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, feel free to reach out to me at [your-email@example.com](mailto:your-email@example.com).

Happy coding!
