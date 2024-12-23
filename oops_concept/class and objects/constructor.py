
# class students:
#     def __init__(self,name,roll,age):
#         self.stu_name=name
#         self.roll=roll
#         self.age=age
#     def display(self):
#         print(self.stu_name)
#         print(self.roll)
#         print(self.age)
#
# obj1=students("jitty",21,26)
# obj1.display()


class library_management:
    def __init__(self,library_name):
        self.libname=library_name
        self.books=[]
    def add_books(self,title):
        self.books.append(title)
    def remove_books(self,title):
        if title in self.books:
            self.books.remove(title)
            print(self.books)
        else:
            print("Book not found")
    def list_books(self):
        print('Library name=',self.libname)
        print(self.books)

obj1=library_management('AKJ lIBRARY')
obj1.add_books('Pride and Prejudice')
obj1.add_books('jane eyre')
obj1.add_books('1984')
obj1.list_books()
obj1.remove_books('jane eyre')




