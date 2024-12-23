# class person:
#     def person_details(self,name,age):
#         self.name=name
#         self.age=age
#     def person_display(self):
#         print("Name=",self.name)
#         print("Age=",self.age)
# class student(person):
#     def student_details(self,roll_no,dept,email):
#         self.roll_no=roll_no
#         self.dept=dept
#         self.email=email
#     def student_display(self):
#         self.person_display()
#         print("Roll no=",self.roll_no)
#         print("Department=",self.dept)
#         print("Email=",self.email)
# obj=student()
# obj.person_details("Jitty",26)
# obj.student_details(25,"MCA","jittysjohn1997@gmail.com")
# obj.student_display()
#
# #
# class vehicle:
#     def vehicle_details(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#     def display_info(self):
#         print("make=",self.make)
#         print("model=",self.model)
#         print("year=",self.year)
# class car(vehicle):
#     def additional_info(self,no_of_doors,fuel_type):
#         self.no_of_doors=no_of_doors
#         self.fuel_type=fuel_type
#     def complete_details(self):
#         self.display_info()
#         print("no: of doors=",self.no_of_doors)
#         print("fuel_type=",self.fuel_type)
# obj1=car()
# obj1.vehicle_details("Honda","Civic",2021)
# obj1.additional_info(4,"Gasoline")
# obj1.complete_details()


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def person_display(self):
#         print("Name=",self.name)
#         print("Age=",self.age)
# class student(person):
#     def __init__(self,name,age,roll_no,dept,email):
#         super().__init__(name,age)
#         self.roll_no=roll_no
#         self.dept=dept
#         self.email=email
#     def student_display(self):
#         self.person_display()
#         print("Roll no=",self.roll_no)
#         print("Department=",self.dept)
#         print("Email=",self.email)
# obj3=student("Jitty",26,25,"MCA","jittysjohn1997@gmail.com")
# obj3.student_display()



class vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print("make=",self.make)
        print("model=",self.model)
        print("year=",self.year)
class car(vehicle):
    def __init__(self,make,model,year,no_of_doors,fuel_type):
        super().__init__(make,model,year)
        self.no_of_doors=no_of_doors
        self.fuel_type=fuel_type
    def complete_details(self):
        self.display_info()
        print("no: of doors=",self.no_of_doors)
        print("fuel_type=",self.fuel_type)
obj1=car("Honda","Civic",2021,4,"Gasoline")
obj1.complete_details()