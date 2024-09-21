
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
    total_price = 0   
    for book in books_list : 
                      
        total_price =+ book["price"] 
        
    return total_price
    
def calculate_shiping (books_list ):
  
    if calculate_total (books_list ) < 100:
        
        return " Shipping id freee "
    else:
        return " Shiping is 3.99"

print( calculate_total( books_list )  )
print( calculate_shiping (books_list ) )
    
 



