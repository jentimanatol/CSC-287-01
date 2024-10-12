from ship import Ship

class Port:
    """Initiate class port"""
    
    def __init__(self,port_name,port_id, port_max_dept, max_port_available_spot):
        self.port_name = port_name
        self.port_id = port_id
        self.port_max_dept = port_max_dept
        self.max_port_available_spot = max_port_available_spot
        self.ships = [] 
        self.port_available_spot = max_port_available_spot
        
        
    def add_ship_to_port(self, ship):
        
        if self.port_available_spot > 0 :
            self.port_available_spot = self.port_available_spot-1
            self.ships.append(ship)
        else: 
            print(f"the port is: {self.port_name } is full can not dock the ship")
            
        
    def describe(self):
        """ initialise to sting metod """
        to_string = ''
        for ship in self.ships:
            to_string += ship.describe()
        #print(to_string)
        return f" Port {self.port_name} id number: {self.port_id} with max dept: {self.port_max_dept},and {self.port_available_spot}  available spot out of {self.max_port_available_spot}, docked {to_string} " 
        
        