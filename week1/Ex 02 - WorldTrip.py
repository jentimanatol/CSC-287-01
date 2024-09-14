visitList =  ['US', 'France', 'Italy', 'Germany','Canada']

#- Print out the zeroth element

print(visitList[0])

#- Print out the last element.

print(visitList[-1])

#- Sort the list

visitList.sort()

for i in visitList:
 print({i})

#- Print out each place in the sorted list with an 
#f-string. For example, “I want to go to Paris”, etc.

print ('\n')
for i in visitList:

 print( f"I want to in  {i}  next sumer.")
