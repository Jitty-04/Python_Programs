# if(condition):
#     body of if
# elif(condition):
#     body of elif
# elif(condition):
#     body of elif
# else:
#     body of else

# a=int(input('Enter the number'))
# if(a>0):
#     print('positive')
# elif(a<0):
#     print('negative')
# else:
#     print('zero')
#
# num1=int(input('Enter first number'))
# num2=int(input('Enter Second number'))
# num3=int(input('Enter third number'))
# if(num1>num2 and num1>num3):
#     print(f'{num1} is largest')
# elif(num2>num3):
#     print(f'{num2} is largest')
# else:
#     print(f'{num3} is largest')

# a1=int(input('enter first number'))
# a2=int(input('enter second number'))
# a3=int(input('enter third number'))
# a4=int(input('enter fourth number'))
# if(a1>a2 and a1>a3):
#     if(a1>a4):
#         print(f'{a1} is largest')
# elif(a2>a3 and a2>a4):
#     print(f'{a2} is largest')
# elif(a3>a4):
#     print(f'{a3} is largest')
# else:
#     print(f'{a4} is largest')

# n1=int(input('enter first number'))
# n2=int(input('enter second number'))
# n3=int(input('enter third number'))
# n4=int(input('enter fourth number'))
# n5=int(input('enter fifth number'))
# if(n1<n2 and n1<n3):
#     if(n1<n4 and n1<n5):
#         print(f'{n1} is minimum')
# elif(n2<n3 and n2<n4):
#     if(n2<n5):
#         print(f'{n2} is minimum')
# elif(n3<n4 and n3<n5):
#     print(f'{n3} is minimum')
# elif(n4<n5):
#     print(f'{n4} is minimum')
# else:
#     print(f'{n5} is minimum')

# city=input('Enter the city :')
# if(city=='Delhi'):
#     print('Red Fort')
# elif(city=='Agra'):
#     print('Taj Mahal')
# elif(city=='Jaipur'):
#     print('Jal Mahal')
# else:
#     print('Invalid city')
#
# percent=int(input('Enter the percent'))
# if(91<=percent<=100):
#     print('A+')
# elif(81<=percent<=90):
#     print('A')
# elif(71<=percent<=80):
#     print('B+')
# elif(61<=percent<=70):
#     print('B')
# elif(51<=percent<=60):
#     print('C+')
# elif(41<=percent<=50):
#     print('C')
# elif(31<=percent<=40):
#     print('Just Pass')
# else:
#     print('Failed')

# cost=int(input('enter the cost'))
# if(cost>100000):
#     print(f'Tax is {cost*(15/100)} ')
# elif(50000<cost<=100000):
#     print(f'Tax is {cost*(10/100)}')
# else:
#     print(f'Tax is {cost*(5/100)}')

salary=float(input('Enter ther salary'))
years=int(input('Enter the year '))
if(years>10):
    print(f'Bonus is {salary*(10/100)}')
elif(6<=years<=10):
    print(f'Bonus is {salary*(8/100)}')
else:
    print(f'Bonus is {salary*(5/100)}')



