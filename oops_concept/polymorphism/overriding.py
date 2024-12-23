# class A:
#     def funcionA(self):
#         print('Hello welcome to python')
#
# class B(A):
#     def functionA(self):
#         print('Hello welcome to java ')
# obj=B()
# obj.functionA()
#B functionA overrides A functionA


class Shapes:
    def area(self):
        return 0
class Rectangle(Shapes):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
class Circle(Shapes):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2

obj=Rectangle(6,5)
print("Area of rectangle=",obj.area())
obj2=Circle(5)
print("Area of circle=",obj2.area())


