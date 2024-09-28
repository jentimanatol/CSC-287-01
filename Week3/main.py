
import Amazon.amazon as amazon 


C_plus = {"autor": "Jon",
        "title":"Adjanced Java",
        "price": 10
        }

Java = {"autor": "Jon",
        "title":"Adjanced Java",
        "price": 10
        }

python = {"autor": "Erric Mathes",
        "title":"Python Crash Course",
        "price": 20
        }

books_list =  Java, python, C_plus


#print (books_list)


#amazon.books_list =  Java, python , C_plusm

print("\n Total cost of listed book are       = ", amazon.calculate_total( books_list )  )

print("\n Shiping for the list of book wil be = ",amazon.calculate_shiping (books_list ) , "\n")
    
 