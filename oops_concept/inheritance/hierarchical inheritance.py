# class A:#parent class
#     def funA(self):
#         print('class A')
#
# class B(A):
#     def funB(self):
#         print('class b')
#
# class C(A):
#     def funC(self):
#         print('class C')
#
# obj1=C()
# obj1.funA()
# obj1.funC()
#
# obj2=B()
# obj2.funA()
# obj2.funB()

#Details :name,email,phone
#Doctor:hospital name,specialization(name,email,phone) Doctor-Details
#Engineer:company_name,designation(name,email,phone) Engineer-Details


class Details:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
    def display_details(self):
        print("Name:",self.name)
        print("Email:",self.email)
        print("Phone:",self.phone)
class Doctor(Details):
    def __init__(self,name,email,phone,hospital_name,specialization):
        super().__init__(name,email,phone)
        self.hospital_name=hospital_name
        self.specialization=specialization
    def display_doctor(self):
        self.display_details()
        print('Hospital name:',self.hospital_name)
        print('Specialization:',self.specialization)
class Engineer(Details):
    def __init__(self,name,email,phone,company_name,designation):
        super().__init__(name, email, phone)
        self.company_name=company_name
        self.designation=designation
    def display_engineer(self):
        self.display_details()
        print("Company name:",self.company_name)
        print("Designation:",self.designation)
obj1=Doctor('Sarramma','sarama123@gmail.com',987878989,'Lifeline',"Gynecologist")
obj1.display_doctor()
print()
obj2=Engineer('Jitty','jitty1213@gmail.com',986787879,'TCS','Python Developer')
obj2.display_engineer()