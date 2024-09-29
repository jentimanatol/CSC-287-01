from container import Container 

class Ship:
    """describe clas container """
    def __init__(self,ship_id):
        self.ship_id = ship_id
        self.containers = []
        
        
    def add_container_toSheep(self, container):
        self.containers.append(container)
        
        
    def describe(self):
        to_string = ''
        for container in self.containers:
            to_string += container.describe()
        #print(to_string)
        return f" Ship with identification: {self.ship_id} carry  {to_string} " # [ for box in self.boxes: box.describe() ] #research whay do not allow foor loop
        
        
        