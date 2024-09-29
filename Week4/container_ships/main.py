from box import Box
from container import Container
from ship import Ship
from port import Port

# create boxes item_name, item_id, item_description, items_per_box):
television_box1 = Box("sony O led 55", 656546, "Hig definition 110V american srtandart", 1)
television_box2 = Box("Samsung Q led 65", 635354,  "Hig definition 110V american srtandart", 1)

#create container with :Container company name(cosco , wallmar, Evergreen),  container_id number(int number ) , container_type (moisture profe , refrigerated, open side), container_size (full, half, quater)):
television_container = Container("COSCO",65895,"moisture profe", "full")
#add boxes in container 
television_container.add_box_to_container(television_box1)
television_container.add_box_to_container(television_box2)

#create ship ship_name, ship_id, ship_capacity):
containers_ship1 = Ship("Capitan Nellson", 65684, 1000)
#containers_ship2 = Ship("Ever Green", 65684, 1000)

#add A CONTAINER TO THE SHIIP

containers_ship1.add_container_toSheep(television_container)


#CREATE A PORT with name , id and max dept in feet, port_available_spot

atlantic_port1 = Port("Boston Harbor", 2356, 25, 10)

#add ship to the port
atlantic_port1.add_ship_to_port(containers_ship1)
#atlantic_port1.add_ship_to_port(containers_ship2)


#to string port detail 

print("\n",atlantic_port1.describe())

