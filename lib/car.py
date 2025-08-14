from vehicle import Vehicle

class Car(Vehicle): 
    def go(self):   
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

my_car = Car(48, 4)
print(my_car.go()) 