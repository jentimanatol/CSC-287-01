#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket. Typing quit should exit the program.
#Also try using a flag or the break statement to implement the above.


flag = True 
age = 0

while flag:
    msg = input (" Print the age ")
    
    if msg =='quit':
       flag = False
       print ("you just exit the aplication")
    else:
        age = int(msg)

       
        if age <=3 :     
               print ("the ticket is free ")
           
        elif age < 12 : 
             print("the ticket is $10") 
         
        else  : print("the ticket is $15") 
    
    
           
       
       
   