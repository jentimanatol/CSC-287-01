
"""Create a script Ex 05 - Amazon.py
Create a dictionary for storing attributes of a book, e.g. author, title, and price.
Create a list of books and put two books in the list.

Create a function called calculate_total() that takes a list of books and calculates the 
total price of all the books.

Create a function called calculate_shipping() that takes a total price and:
If the total price is >$100, return 0.00 (shipping is free!)
Otherwise, returns $3.99.
Prompt the user if they want to checkout.  If they say yes, print out the total number 
of books and the final total price.  Otherwise, print out “Come back soon!”
"""

Java = {"autor": "Jon",
        "title":"Adjanced Java",
        "price": 10
        }

python = {"autor": "Erric Mathes",
        "title":"Python Crash Course",
        "price": 20
        }


books_list =  Java, python


print (books_list)


def calculate_total (books_list ):

    
    for i in books_list :
        
        print (books_list.autor[i])
    


calculate_total( books_list )  
    
 



