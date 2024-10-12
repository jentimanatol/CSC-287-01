from box import Box
class Container:
    def __init__(self,container_company_name, container_id, container_type, container_size):
        """initializate container classs"""
        self.container_company_name = container_company_name 
        self.container_id = container_id
        self.container_type = container_type
        self.container_size = container_size
        
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
        #print(to_string,"\n")
        return f"container named: {self.container_company_name} with id number: {self.container_id}, tipe: {self.container_type}, size: {self.container_size}, contain: {to_string}." 
        
        
    