"""""Create a sub-folder named Amazon within the Week-03 folder
From the previous exercise, create a new amazon.py module and add in the calculate_total() and calculate_shipping() methods.
Then, move the rest of your code into a main.py module, and import amazon.
Verify that your code works exactly the same as Exercise #1.
"""


def calculate_total ( books_list  ):
    total_price = 0   
    for book in books_list : 
                      
        total_price =+ book["price"] 
        
    return total_price
    
    
def calculate_shiping (books_list ):
  
    if calculate_total (books_list ) < 100:
        
        return " Shipping is freee "
    else:
        return " Shiping is 3.99"