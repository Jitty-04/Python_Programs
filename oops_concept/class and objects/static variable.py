#create a class company with two static variables company_name and location
#1.employee_details() with attributes emp_id,emp_name,designation,salary
#2.employee_display()
#company name = TCS
#company loc = kakkanad
#employee id = 123
#employee name=akhil
#designation = Tester
#salary = 18000
#
#
# class company:
#     company_name='TCS'
#     location='kakkanad'
#
#     def employee_details(self,emp_id,emp_name,designation,salary):
#         self.emp_id=emp_id
#         self.emp_name=emp_name
#         self.designation=designation
#         self.salary=salary
#
#     def employee_display(self):
#         print("company name=",company.company_name)
#         print("location=",company.location)
#         print("employee id=",self.emp_id)
#         print("employee name=",self.emp_name)
#         print("designation=",self.designation)
#         print("salary=",self.salary)
#
# obj1=company()
# obj1.employee_details(123,"Jitty","Tester",18000)
# obj1.employee_display()



#
# class Bank_Account:
#     bank_name='SBI'
#     branch='Adoor'
#     def set_account_info(self,ac_num,ac_holder):
#         self.ac_num=ac_num
#         self.ac_holder=ac_holder
#         self.balance=0
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f'{amount} deposited,balance=',self.balance)
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print(f"{amount} withdrawed, balance=",self.balance)
#         else:
#             print("insufficient balance")
#     def account_info(self):
#         print("Bank name=",Bank_Account.bank_name)
#         print("Branch=",Bank_Account.branch)
#         print("Account Number=",self.ac_num)
#         print("Account Holder=",self.ac_holder)
#         print("Balance=",self.balance)
#     def check_balance(self):
#         print("Current Balance=",self.balance)
#
#
# obj1=Bank_Account()
# obj1.set_account_info(12345,'Jitty')
# obj1.account_info()
# obj1.deposit(5000)
# obj1.withdraw(1000)
# obj1.withdraw(5000)
# obj1.account_info()
# obj1.check_balance()





