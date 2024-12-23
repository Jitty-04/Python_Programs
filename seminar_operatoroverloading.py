# # print(dir(int))
#
# mystring='jitty'
# print(mystring.__len__())
# # a=1
# # b=2
# # print(a+b)
#
# result=(1).__add__(2)
# print(result)
#
# class car:
#     def __init__(self,name,price,kilometers):
#         self.name=name
#         self.price=price
#         self.kilometers=kilometers
#     def __len__(self):
#         return self.kilometers
# car1=car('Swift',120000000,30000000)
# print(len(car1))

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __mul__(self, scalar):
#         return Vector(self.x * scalar, self.y * scalar)
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
# # Create a vector
# vect = Vector(4, 5)
#
# # Multiply the vector by a scalar
# vect_scaled = vect * 4
#
# print("Original Vector:", vect)
# print("Scaled Vector (vect * 4):", vect_scaled)

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         return self.area() == other.area()
#
# # Create two rectangles
# rectangle1 = Rectangle(6, 8)
# rectangle2 = Rectangle(2, 24)
#
# # Compare the two rectangles
# print("Rectangle 1 area:", rectangle1.area())
# print("Rectangle 2 area:", rectangle2.area())
# print("Are the two rectangles equal in area?", rectangle1 == rectangle2)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

# Create two bank accounts
acc1 = BankAccount(2000)
acc2 = BankAccount(1500)

# Compare the two accounts
print("Account 1 balance:", acc1.balance)
print("Account 2 balance:", acc2.balance)
print("Is Account 1 balance greater than Account 2?", acc1 > acc2)
print("Is Account 1 balance less than Account 2?", acc1 < acc2)











