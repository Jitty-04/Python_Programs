# class encapsulation:
#     def __init__(self,name,address,phone):
#         self.name=name #public data member
#         self._address=address #protected
#         self.__phone=phone #private
#     def display(self):
#         print()
#     def _display(self):
#         print()
#     def __display(self):
#         print()

#public access modifier
#
# class person:
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email
#     def display(self):
#         print("Name: ",self.name)
#         print("Email: ",self.email)
# obj=person('Jitty','jitty12@gmail.com')
# obj.display()
# print()
# print(obj.name)
# print()
# obj.name="Delisa"
# obj.email="delisa123@gmail.com"
# obj.display()

# class person:
#     def __init__(self,name,email):
#         self.__name=name
#         self.__email=email
#     def __display(self):
#         print("Name: ",self.__name)
#         print("Email: ",self.__email)
# obj=person('Jitty','jitty12@gmail.com')
# # print(obj.name)
# print(obj._person__name)# name mangling
# print(obj._person__email)#_classname__datamember
# print()
# obj._person__name="Delisa"
# obj._person__email="delisa123@gmail.com"
# obj._person__display()


class person:
    def __init__(self,name,email):
        self._name=name
        self._email=email
    def _display(self):
        print("Name: ",self._name)
        print("Email: ",self._email)
obj=person('Jitty','jitty12@gmail.com')
print(obj._name)
print(obj._email)
print()
obj._name="Delisa"
obj._email="Delisa12@gmail.com"
obj._display()




































