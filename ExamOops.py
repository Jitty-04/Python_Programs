# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#     def update_grade(self,new_grade):
#         self.grade=new_grade
#     def is_passing(self):
#         if(self.grade in 'ABC'):
#             return True;
#         else:
#             return False;
#     def get_student_info(self):
#         print('Name:',self.name ,'Age:',self.age,'Grade:',self.grade,'pass:',self.is_passing())
#
# obj1=Student("Jitty",26,'B')
# obj2=Student("Libin",27,'A')
# obj3=Student("Delisa",20,'C')
# obj1.update_grade('D')
# obj1.get_student_info()
# obj2.get_student_info()
# obj3.get_student_info()
from itertools import count


class Movie:
    def __init__(self,title,rating):
        self.__title=title
        self.__rating=rating
        self.__reviews=[]
    def __add_review(self,review):
        self.__reviews.append(review)

    def __get_reviews(self):
        return self.__reviews.copy()

    def __set_rating(self,new_rating):
        if (1.0<new_rating<5.0):
            self.rating=new_rating
        else:
            print("Error:rating must be between 1.0 and 5.0")
    def __get_info(self):
        return f"Title:{self.__title},Rating:{self.__rating},Reviews:{len(self.__reviews)}"
ob=Movie("omshasnti",3)
ob._Movie__add_review("Good")
ob._Movie__add_review("Nice")
print(ob._Movie__get_info())
print(ob._Movie__get_reviews())
print(ob._Movie__set_rating(4))
print(ob._Movie__get_info())











