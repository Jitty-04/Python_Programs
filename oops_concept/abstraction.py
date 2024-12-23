from abc import ABC,abstractmethod# abc package,ABC module

class Shapes(ABC):#ABSTRACT CLASSS where ABc is base class with hidden content
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shapes):
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)

class Circle(Shapes):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*(self.radius**2)
    def perimeter(self):
        return 2*3.14*self.radius

obj=Rectangle(2,4)
print('Area of rectangle=',obj.area())
print('perimeter of rectangle=',obj.perimeter())
obj1=Circle(5)
print("Area of circle=",obj1.area())
print("Perimeter of circle=",obj1.perimeter())






