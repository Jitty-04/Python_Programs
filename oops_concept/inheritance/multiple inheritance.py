


# class school:
#     def school_details(self,school_name,location):
#         self.school_name=school_name
#         self.location=location
#     def school_display(self):
#         print('school name=',self.school_name)
#         print('location=',self.location)
# class parent:
#     def parent_details(self,parent_name,address):
#         self.parent_name=parent_name
#         self.address=address
#     def parent_display(self):
#         print('Parent name=',self.parent_name)
#         print('Address=',self.address)
# class student(school,parent):
#     def student_details(self,rollno,name,dept):
#         self.rollno=rollno
#         self.name=name
#         self.dept=dept
#     def student_display(self):
#         print('Roll no:=',self.rollno)
#         print('name=',self.name)
#         print('dept=',self.dept)
#     def view_complete_details(self):
#         self.school_display()
#         self.parent_display()
#         self.student_display()
# obj=student()
# obj.school_details("CASA","Adoor")
# obj.parent_details("Saji","Saji nivas")
# obj.student_details(25,"Jitty","MCA")
# obj.view_complete_details()
# class company:
#     def __init__(self,company_name,location):
#         self.company_name=company_name
#         self.location=location
#     def company_display(self):
#         print("company name=",self.company_name)
#         print("location=",self.location)
# class team_leader:
#     def __init__(self,team_leader_name,dept):
#         self.team_leader_name=team_leader_name
#         self.dept=dept
#     def teamleader_display(self):
#         print('team leader name=',self.team_leader_name)
#         print('dept=',self.dept)
# class worker(company,team_leader):
#     def __init__(self,company_name,location,team_leader_name,dept,emp_name,designation,salary):
#         company.__init__(self,company_name,location)
#         team_leader.__init__(self,team_leader_name,dept)
#         self.emp_name=emp_name
#         self.designation=designation
#         self.salary=salary
#     def worker_display(self):
#         print("employee name=",self.emp_name)
#         print("designation=",self.designation)
#         print("salary=",self.salary)
#     def complete_detail(self):
#         self.company_display()
#         self.teamleader_display()
#         self.worker_display()
# obj=worker("Nest Digital","EKM",'Libin','IT',"Jitty","Developer",50000)
# obj.complete_detail()






