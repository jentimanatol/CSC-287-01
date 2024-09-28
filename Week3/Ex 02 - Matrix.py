#Write a script Ex 02 - Matrix.py that asks for a number between 2 and 9
#If the number is between 2 and 9, print a square matrix of that dimension with 0s as the values
#Eg: Matrix size (2-9): 4
#Output:          0 0 0 0                 0 0 0 0                 0 0 0 0                 0 0 0 0
#If the number is out of bounds, inform the user and exit.


messages = input(" introduce a number between 2 and 9 \n ")
number = int(messages)

matrix = []
if number > 1 and number < 10 :
    for i in range (number):
        for j in range (number):
            matrix.append( 0 )
#print(matrix)


for i in range (number):
      
    for j in range (number):
        
      #  print(f" {matrix[j]} ")  
      print(matrix[j])
      
    print("\n")







