""" 
We are going to be building a very simple Notes application to store notes.
First, create a class called Note.
The __init__ method should store two attributes: id and url.
Write a method called describe() that prints the id and url.
Once your class is done, instantiate three different notes.
Once that is done, verify that it is working.
"""

class Notes:
    """ Initialise"""   
    def __init__(self, id, url): 
        """ Initialise"""
        self.id = id
        self.url = url
        
    def describe(self):
           """ init"""
           print(f"Describe metod to String -> id: {self.id} URL: {self.url} \n")
                    
pc = Notes( 5865, 'www.gmail.com' )   
router = Notes( 50265, 'www.gethub.com' )     
    
print(f"Notes id  {pc.id}.")
print(f"Notes url  {pc.url}.")
pc.describe()

print(f"Notes id  {router.id}.")
print(f"Notes url  {router.url}.")
router.describe()