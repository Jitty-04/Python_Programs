# try:
#     li=['a','b','c','d']
#     index=int(input('enter index position'))
#     print(li[index])
# except IndexError as err:
#     print(err)
#
# except ValueError as a:
#     print(a)

try:
    age=int(input("enter the age"))
    if age>=18:
        print("registered")
    else:
        raise ValueError('plz input age greater than 17')
except ValueError as e:
    print(e)

# num=int(input('enter a number'))
# assert num>0,"Negative number"
# print("possitive number")
# try:
#     num=int(input('enter the number'))
#     assert num>0,"Negative number"
#     print("possitive number")
# except AssertionError as e:
#     print(e)

# try:
#     a=int(input("enter a"))
#     b=int(input("enter b"))
#
# except ValueError as e:
#     print(e)
#
# else:
#     print(a/b)
#
# finally:
#     print("program completed")



