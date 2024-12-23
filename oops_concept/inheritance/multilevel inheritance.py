class vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print('make=',self.make)
        print('model=',self.model)
        print('year=',self.year)
class car(vehicle):
    def __init__(self,num_doors):
        self.num_doors=num_doors
    def display_car_info(self):
        print("num of doors=",self.num_doors)
class electric_car(car):
    def __init__(self,make,model,year,num_doors,battery_capacity):
        vehicle.__init__(self,make,model,year)
        car.__init__(self,num_doors)
        self.battery_capacity=battery_capacity
    def display(self):
        print("battery capacity=",self.battery_capacity)
    def complete_display(self):
        self.display_info()
        self.display_car_info()
        self.display()
obj=electric_car("Honda","Civic",2021,4,1200)
obj.complete_display()
