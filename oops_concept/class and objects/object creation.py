#In oops self is a default instance that is used as the first parameter to allow access to the objects attributes and other methods

class Person:
    def create_person(self,name,age,gender): #create a object
        self.name=name #public
        self.age=age
        self.gender=gender

    def display_person(self):
        print('Name=',self.name)
        print('Age=',self.age)
        print('Gender=',self.gender)

op1=Person()
op1.create_person(name='Jitty',age=26,gender='female')

op2=Person()
op2.create_person(name='libin',age=32,gender='male')

op1.display_person()
op2.display_person()





