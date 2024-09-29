from container import Container 

class Ship:
    """describe clas container """
    def __init__(self,ship_name, ship_id, ship_capacity):
        self.ship_name = ship_name
        self.ship_id = ship_id
        self.ship_capacity = ship_capacity
        self.containers = []
        self._capacity_left = ship_capacity  #private onli metod  add_container_toSheep can modify 
        
        
    def add_container_toSheep(self, container):
        if self._capacity_left > 0 :
            self._capacity_left = self._capacity_left-1
            self.containers.append(container)
        else: 
            print(f"the ship: {self.ship_name } is full cantainer can't be added")
            
        
        
    def describe(self):
        to_string = ''
        for container in self.containers:
            to_string += container.describe()
        #print(to_string)
        return f"Ship Named: {self.ship_name}, with identification number: {self.ship_id}, capacity {self._capacity_left} teft from: {self.ship_capacity} containers, carry  {to_string} " # [ for box in self.boxes: box.describe() ] #research whay do not allow foor loop
        
        
        