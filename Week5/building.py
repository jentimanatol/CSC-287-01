from rooms import Rooms
class Building:
    def __init__(self,building_name):
        """initializate cbuilding classs"""
        self.building_name = building_name 
      
        
        self.rooms = []
        

    def add_romms(self, room):
        """Initiate metod add_box_to_container to ading one motre box in the container """
        #sql_add_box_to_container()
        self.rooms.append(room)
        
        
    def describe(self):
        """ initialise to sting metod """
    
        return f"Building {self.building_name} with id number: {self.room}." 
        
        
    