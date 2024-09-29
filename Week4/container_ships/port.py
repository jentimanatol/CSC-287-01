from ship import Ship

class Port:
    """Initiate class port"""
    def __init__(self,port_name,port_id, port_max_dept):
        self.port_name = port_name
        self.port_id = port_id
        self.port_max_dept = port_max_dept
        self.ships = [] 
        
        
    def add_ship_to_port(self, ship):
        self.ships.append(ship)
        
        
    
    def describe(self):
        """ initialise to sting metod """
        to_string = ''
        for ship in self.ships:
            to_string += ship.describe()
        #print(to_string)
        return f" Port {self.port_name} id number: {self.port_id} with max dept: {self.port_max_dept} docked {to_string} " 
        
        