from box import Box
from container import Container
from ship import Ship
from port import Port

# create boxes 
television_box1 = Box("sony o led 55")
television_box2 = Box("sony Q led 65")

#create container 

television_container = Container("tv_container")
#add boxes in container 
television_container.add_box_to_container(television_box1)
television_container.add_box_to_container(television_box2)

#create ship 
containers_ship1 = Ship("Cargo 2015")

#add A CONTAINER TO THE SHIIP

containers_ship1.add_container_toSheep(television_container)


#CREATE A PORT 

atlantic_port1 = Port("Boston Harbor")

#add ship to the port
atlantic_port1.add_ship_to_port(containers_ship1)


#to string port detail 

print(atlantic_port1.describe())

