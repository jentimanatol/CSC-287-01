#displaysTell me something, and I will repeat it back to you:Enter 'quit' to end the program.
#Accepts whatever the user types, and prints it right back.
#If the user types quit then exit the program



flag = True 

while flag:
    msg = input (" Tell me something, and I will repeat it back to you:Enter 'quit' to end the program.")
    
    if msg =='quit':
       flag = False
       print("aplication wasa closetd.")
       
    else : print (msg)
       
    