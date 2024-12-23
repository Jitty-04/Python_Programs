import time
from time import strftime

#localtime
# print(time.localtime())

# x=time.localtime()
# print("year=",x.tm_year)
# print("month=",x.tm_mon)

#asctime():human readable time format
# print(time.asctime())

#sleep()
# print("hello welcome")
# print(time.sleep(2.5))#seconds
# print('print after 2.5 sec')

#strftime()   string formattime
print(time.strftime('%A'))
print(time.strftime('%a'))
print(time.strftime('%B'))
print(time.strftime(('%D')))
print(time.strftime('%d'))
print(time.strftime('%Y'))
print(time.strftime('%H'))
print(time.strftime('%M'))
print(time.strftime('%S'))
print(time.strftime('%m'))

print(time.strftime('%a %H:%M:%S %Y' ))

