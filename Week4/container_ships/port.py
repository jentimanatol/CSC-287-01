from ship import Ship

class Port:
    """Initiate class port"""
    def __init__(self,port_id):
        self.port_id = port_id
        self.ships = [] 
        
        
    def add_ship_to_port(self, ship):
        self.ships.append(ship)
        
        
    
    def describe(self):
        """ initialise to sting metod """
        to_string = ''
        for ship in self.ships:
            to_string += ship.describe()
        #print(to_string)
        return f" Port with id number: {self.port_id} contain {to_string} " 
        
        