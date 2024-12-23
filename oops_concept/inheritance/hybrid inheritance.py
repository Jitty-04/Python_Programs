# class baseclass:
#     def funBase(self):
#         print('Base class')
#
# class A(baseclass):
#     def funA(self):
#         print('Class A')
#
# class B(baseclass):
#     def funB(self):
#         print('Class B')
#
# class C(A,B):
#     def funC(self):
#         print('Class C')
#
# obj=C()
# obj.funBase()
# obj.funA()
# obj.funB()
# obj.funC()


# university:uni_name,location
# university_info()
#
# A:undergraduateprogram:name_of_ug_students,ug_course(u)
#
# B:postgraduateprogram:name_of_pg_students,pg_project(u)
#
# C:programdirector : director_name(A,B)


class university:
    def __init__(self,uni_name,location):
        self.uni_name=uni_name
        self.location=location
    def university_info(self):
        print("University Name: ",self.uni_name)
        print("Location: ",self.location)
class undergraduateprogram(university):
    def __int__(self,uni_name,location,name_of_ug_student,ug_course):
        university.__init__(self,uni_name,location)
        self.name_of_ug_student=name_of_ug_student
        self.ug_course=ug_course
    def undergraduateprogram_info(self):
        self.university_info()
        print("Name of Ug Student: ",self.name_of_ug_student)
        print("Ug Course: ",self.ug_course)
class postgraduateprogram(university):
    def __init__(self,uni_name,loaction,name_of_pg_student,pg_project):
        university.__init__(self,uni_name,loaction)
        self.name_of_pg_student=name_of_pg_student
        self.pg_project=pg_project
    def postgraduateprogram_info(self):
        self.university_info()
        print("Name of Pg Student: ",self.name_of_pg_student)
        print("Pg Project: ",self.pg_project )
class director(undergraduateprogram,postgraduateprogram):
    def __init__(self,uni_name,location,name_of_ug_student,ug_course,name_of_pg_student,pg_project,director_name):
        undergraduateprogram.__int__(self,uni_name,location,name_of_ug_student,ug_course)
        postgraduateprogram.__init__(self,uni_name,location,name_of_pg_student,pg_project)
        self.director_name=director_name
    def director_display(self):
        self.undergraduateprogram_info()
        self.postgraduateprogram_info()
        print("Director Name: ",self.director_name)
obj=director("KTU","TVM","Jitty","MCA","Sara","Cyberspy","Hima")
obj.university_info()
print()
obj.undergraduateprogram_info()
print()
obj.postgraduateprogram_info()
print()
obj.director_display()










