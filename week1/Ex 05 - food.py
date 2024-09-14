
# Create a program that stores all your favorite foods into a list called foods. 
#Store all your foods in lowercase, e.g. “pizza”, “cheeseburgers”, etc.
#Print each item in foods.
food_list = ['pizza', 'lazzaniA', 'pasta', 'burgers']
print(food_list)

#Create a new variable called foods_upper and use it to store the upper case 

upper_food_list = []
#for i in range (0 , food_list.lenght):  
for i in range(0, len(food_list)):  
    upper_food_list.append( food_list[i].upper()    )   
print(upper_food_list)


#Print out different slices of foods. For example, try printing out the first 
#two items.
print (upper_food_list[0:2])


#Sort and print the foods list. #version of all your foods, e.g “PIZZA”, etc.

upper_food_list.sort()
print (upper_food_list)

#Bonus: do the last part as a list comprehension.