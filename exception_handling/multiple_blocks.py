# try:
#     a=int(input("enter a:"))
#     b=int(input('enter b:'))
#     print(a/b)
# except ZeroDivisionError:
#     print("can't divide by zero")
#
# except ValueError:
#     print("enter interger value")

#quadratic equation
try:
    a=int(input('enter a:'))
    b=int(input('enter b:'))
    c=int(input('enter c:'))
    d=(b**2-4*a*c)**0.5
    x1=(-b+d)/(2*a)
    x2=(-b-d)/(2*a)
    print(f'{x1,x2}')
except ValueError:
    print('enter integer value')
except ZeroDivisionError:
    print("can't divide by zero")

