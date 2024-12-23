# class Maths:
#     def add(self,a,b):
#         print(a+b)
#
#     def add(self,a,b,c):
#         print(a+b+c)
#
# obj=Maths()
# obj.add(2,4,3)


# decorator
#  function extended without any modification

from multipledispatch import dispatch

# class Maths:
#     @dispatch(int,int)
#     def add(self,a,b):
#         print(a+b)
#
#     @dispatch(int,int,int)
#     def add(self,a,b,c):
#         print(a+b+c)
#
# obj=Maths()
# obj.add(2,4)
# obj.add(2,3,4)




#create a function length() using overloading method:length(str),length(list),length(tuple),length(set),length(dict)||dont use len()
from multipledispatch import dispatch
class datatype_length:
    @dispatch(str)
    def length(self,str):
        c=0
        for i in str:
            c+=1
        print(f'length={c}')

    @dispatch(list)
    def length(self,li):
        c=0
        for i in li:
            c+=1
        print(f'length={c}')

    @dispatch(set)
    def length(self,s):
        c=0
        for i in s:
            c+=1
        print(f"length={c}")

    @dispatch(tuple)
    def length(self,t):
        c=0
        for i in t:
            c+=1
        print(f"length={c}")

    @dispatch(dict)
    def length(self,d):
        c=0
        for i in d:
            c+=1
        print(f"Length={c}")
obj=datatype_length
obj.length("Jitty")
obj.length([1,7,0,'a'])
obj.length({3,8,9})
obj.length((7,9,0,4,6))
obj.length({'a':'JITTY','b':'DELISA'})




