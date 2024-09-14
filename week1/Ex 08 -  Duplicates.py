#Initialize a list that contains duplicate 
#elements. Ex. [1, 2, 3, 2, "one", 3, 2, "two", 
#6, 8, 1, "two", "four", 8, 12].
#3Using what you have learned so far, create 
#another list from this that only contains unique 
#values

duplicate_elements =  [1, 2, 3, 2, "one", 3, 2, "two", 6, 8, 1, "two", "four", 8, 12]

unic_elements = []


for i in duplicate_elements:
    
    if i not in unic_elements :
    
      unic_elements.append(i)
      
print(unic_elements)



ro_dict = {"unu":"one", "dou":"two","trei":"tree" }

print(ro_dict["unu"])


print(f"translation on the word unu in ro is {ro_dict["unu"]}" )

