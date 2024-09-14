car_brands = ['toyota', 'audi', 'honda', 'bmw', 'ford', 'chrysler', 'tesla']

for i in range(len(car_brands)):
    
    if car_brands[i] == 'bmw':
        
        car_brands[i] = car_brands[i].upper()
    else:
        car_brands[i] = car_brands[i].capitalize()

print(car_brands)