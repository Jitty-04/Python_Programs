#ZeroDivisionError
# try:
#     a=int(input('enter a:'))
#     b=int(input('enter b:'))
#     print(a/b)
#
# except:
#     print("can't divide a number by zero")

#ValueError
# try:
#     num=int(input('enter number'))
#     print(num)
# except:
#     print('plz enter integer value')

#indexerror
try:
    list=['a','b','c','d']
    index=int(input('enter the index'))
    print(list[index])
except:
    print("index out of range")