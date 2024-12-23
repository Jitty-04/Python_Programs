# class class_name:
#     body of class

# class first:
#     def hello(self):
#         print('welcome to oops')
#
# x=first()
# x.hello() #x is known as reference variable

#function defined inside class is known as methos or member functions

#create a class calculator with 4 methods add,sub,multiply and div that passes 2 arguments

class Calculator:
    def add(self,a,b):
        print(a+b)

    def sub(self,a,b):
        print(a-b)

    def mul(self,a,b):
        print(a*b)

    def div(self,a,b):
        print(a/b)

op=Calculator()
op.add(6,2)
op.sub(8,2)
op.mul(4,3)
op.div(6,2)


