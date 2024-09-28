from box import Box
class Container:
    def __init__(self,container_id):
        """initializate container classs"""
        self.container_id = container_id
        self.boxes = []
        
    def add_box_to_container(self, box):
        """Initiate metod add_box_to_container to ading one motre box in the container """
        #sql_add_box_to_container()
        self.boxes.append(box)
        
        
    def describe(self):
        """ initialise to sting metod """
        to_string = ''
        for box in self.boxes:
            to_string += box.describe()
        print(to_string,"\n")
        return f" Container with id number: {self.container_id} contain {to_string} " 
        
        
    