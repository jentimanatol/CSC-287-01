""""Now imagine that your Notes application can store two different kinds of notes: 
TextNotes and PhotoNotes.
Write a class named TextNote that extends your previous Note class. 
The init() method should take an additional attribute, named text.  
Override the describe() method to print the note ID, note URL and note Text.
Write a class named PhotoNote that extends your previous Note class.  
The init() method should take an additional attribute, named caption. 
Override the describe() method to print the note ID, note URL and caption.
Create an example TextNote and PhotoNote and call describe() on each."""

#----------------------------
class Nodes:
    """ Initialise"""
    
    def __init__(self, id, url): 
        """ Initialise"""
        self.id = id
        self.url = url
        
    def describe(self):
           """ init"""   
           
           return f" id number = {self.id} , url is : {self.url}."       
#-------------------------------------------------         

class TextNote(Nodes):
    """Init clas text node"""
    
    def __init__(self, id, url, text): 
        
        """Initialise atribute of the parent clas """
        super().__init__( id, url )
        self.text = text
        
        
    def describe(self):
           """ Over-ride description """
           
           return f"{super().describe()}, text = { self.text }."
       
server1 = TextNote( 5865, 'www.gmail.com', ' text saved ')
print("\n")
print(f"Opened node id  :  {server1.id}.")
print(f"Opened node url :  {server1.url}.")
print(f"Opened node url :  {server1.text}.")

print("\n" , server1.describe())
print("\n")
