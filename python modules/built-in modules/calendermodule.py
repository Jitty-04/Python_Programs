import calendar

year=int(input('enter the year:'))
month=int(input('enter the month:'))
print(calendar.month(year,month))

year=int(input('enter the year:'))
print(calendar.calendar(year))

#isleap()
print(calendar.isleap(2024))

#TEXTCALENDER
x=calendar.TextCalendar(calendar.SUNDAY)
print(x.formatyear(2024))
print(x.formatmonth(2014,10))


