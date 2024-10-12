"""Download the Titanic data set from:  https://raw.githubusercontent.com/ecerami/oopl/main/python/files/data/titanic.csv
Write a Python program that reads the titanic data set and prints everything to the screen.
Update your program to count and display the total number of lines in the file.

Update your program to display only the names of the passengers.  Hint:  consider using the split() method.

[Think on this one…]  Update your program to summarize the number of passengers in first class, second class, and third 
class and output this to a file called “summary.txt”. (think on this one a bit;  there are multiple ways to do this…)
"""


import os
import sys
import glob, re

# Open the file and read into a list of lines.
with open('./titanic.csv', encoding="utf-8") as f:
    lines = f.readlines()

# Iterate through all the lines.
# Output includes the line number.
line_num = 0
for line in lines:
    print(f"{line_num}:  {line.rstrip()}")
    line_num += 1

# print(f'\n Total Number of line : {line_num}')


##################################
one_line_variable = '2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C'

test1 = one_line_variable.split('"')

# print(test1[1])

###################################
index = 0
for line in lines:
    if(index ==0):
       continue
    test1 = line.split('"')

    print(test1[1]) 
    
    index +=1





    
