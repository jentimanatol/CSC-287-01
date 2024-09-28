""" We are going to be building a very simple Notes application to 
store notes.
First, create a class called Note.
The __init__ method should store two attributes: id and url.
Write a method called describe() that prints the id and url.
Once your class is done, instantiate three different notes.
Once that is done, verify that it is working."""

class Nodes:
    """ Initialise"""
    
    def __init__(self, id, url): 
        """ Initialise"""
        self.id = id
        self.url = url
        
    def describe(self):
           """ init"""
           print(f"{self.id} is now sitting.")
           print(f"{self.url} is now sitting.")
           
           
           
           
pc = Nodes( 5865, 'www.gmail.com' )   
router = Nodes( 50265, 'www.gethub.com' )   
     
    
print(f"Opened node id  {pc.id}.")
print(f"Opened node url  {pc.url}.")

print(f"Opened node id  {router.id}.")
print(f"Opened node url  {router.url}.")