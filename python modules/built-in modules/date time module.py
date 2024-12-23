import datetime
print(datetime.date.today())#display date

print(datetime.datetime.now())#display date and time

#timedelta()
x=datetime.date.today()
x+=datetime.timedelta(days=10)
print(x)

y=datetime.date.today()
y-=datetime.timedelta(days=100)
print(y)








