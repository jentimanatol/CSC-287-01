
""""
Now imagine that your Notes application can store two different kinds of notes: 
TextNotes and PhotoNotes.

Write a class named TextNote that extends your previous Note class. 
The init() method should take an additional attribute, named text.  
Override the describe() method to print the note ID, note URL and note Text.

Write a class named PhotoNote that extends your previous Note class.  
The init() method should take an additional attribute, named caption. 
Override the describe() method to print the note ID, note URL and caption.
Create an example TextNote and PhotoNote and call describe() on each.
"""

#----------------------------
class Notes:
    """ Initialise"""
    
    def __init__(self, id, url): 
        """ Initialise"""
        self.id = id
        self.url = url
        
    def describe(self):
           """ init"""   
           
           return f" Note Id: {self.id}, from: {self.url}"       
#-------------------------------------------------         

class TextNote(Notes):
    """Init clas text node"""
    
    def __init__(self, id, url, text): 
        
        """Initialise atribute of the parent clas """
        super().__init__( id, url )
        self.text = text
        
        
    def describe(self):
           """ Over-ride description """
           
           return f" {super().describe()}, contain text: { self.text }."
       
#----------------------------------------------------------------------------
class PhotoNote(Notes):
    """Init clas text PhotoNote"""
    
    def __init__(self, id, url, caption): 
        
        """Initialise atribute of the parent clas """
        super().__init__( id, url )
        self.caption = caption
        
        
    def describe(self):
           """ Over-ride description """
           
           return f"{super().describe()}, contain caption: { self.caption }."
       
#------------------------------------------------------------------------------
     
server_text1 = TextNote( 5865, 'www.gmail.com', ' contain text note  ')

print(f"Note id  :  {server_text1.id}.")
print(f"Note url :  {server_text1.url}.")
print(f"Note text :  {server_text1.text}.")
print(server_text1.describe(),"\n")

       
server_PhotoNote1 = PhotoNote( 658945, 'www.github.com', ' Photo description.')
print(f"Note id  :  {server_PhotoNote1.id}.")
print(f"Note url :  {server_PhotoNote1.url}.")
print(f"Note caption :  {server_PhotoNote1.caption}.")

print(server_PhotoNote1.describe(),"\n")
