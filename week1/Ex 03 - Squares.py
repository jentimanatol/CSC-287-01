#outputs the the square of the numbers 1 through 10 in a single line.
squarsList = [] 
for i in range (1 ,  10):
  squarsList.append(i*i)   
print(squarsList)
print ('\n')

#How about 1 through 100?
for i in range (1 ,  100):
  squarsList.append(i*i)   
print(squarsList)

#- Now make it print the square of squares of the first 100 numbers.

square_of_squarsList = [] 
for i in squarsList:
  square_of_squarsList.append(i*i)
print(square_of_squarsList)

#- Print the square of squares of the first 20 numbers (hint: use list slicing)
print ('\n')
print(square_of_squarsList[0:20])


#create a list from list using diferit method 
print ('\n')
squarsList = [i*i for i in range(10)]

print(squarsList)



