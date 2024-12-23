# x=lambda a,b: a+b
# print(x(1,2))


# r=lambda a: a**0.5
# print(r(25))
#
# c=lambda b: b**3
# print(c(5))
#
# z=lambda r: 3.14*(r**2)
# print(z(2))
#
# t=lambda b,h: 1/2*b*h
# print(t(7,8))

#condition in lambda
#
# x=lambda a,b:f'{a} is greater' if(a>b) else f'{b} is greater'
# print(x(6,5))
#
#
# x=lambda a:f'{a} is even' if(a%2==0) else f'{a} is odd'
# print(x(6)+'\n'+x(3))
#
# ch=lambda c:f'{c} is a vowel' if(c in 'aeiou') else f'{c} is not a vowel'
#
# a=input('Enter the character').strip()
# print(ch(a))
#
# n=lambda num:f'{num} is a positive number' if(num>0) else f'{num} is a negative number'
# print(n(-9)+'\n'+n(10))

#
#
#
# x=lambda num:"positive" if(num>0) else ("negative" if(num<0) else "zero")
# print(x(5)+'\n'+x(0)+'\n'+x(-7))
#
# x=lambda a,b,c:(a if(a>c) else c) if(a>b) else(b if(b>c) else c  )
# print(f'largest=',x(-9,5,8))
# #
# x=lambda a,b,c,d,e: a if(a<b and a<c and a<d and a<e ) else b if(b<c and b<d and b<e) else c if(c<d and c<e) else d if(d<e) else e
# print(f'min=', x(8,7,6,2,1))
#
# li=[1,2,3,4,5,6]
# x=list(filter(lambda i : i%2 == 0 ,li))
# print(x)
#
# li1=[1,2,'a','b']
# x=list(filter(lambda i: type(i) is str,li1))
# print(x)
#
# li2=eval(input('enter the list of numbers'))
# y=list(filter(lambda j: (j % 2==0 and j % 3 == 0),li2))
# print(y)
#
# str=input('enter the string')
# s=list(filter(lambda k: k in 'aeiouAEIOU',str))
# print(s)







# li=[1,2,3,4]
# x=list(map(lambda i:i**2,li))
# print(x)
#
# li1=["welcome","hello","python"]
# x=list(map(lambda i: str(i).title(),li1))
# print(x)
#
#
# list1=eval(input('enter the strings'))
# x=list(map(lambda i:i[::-1],list1))
# print(x)
#

from _functools import reduce

li=[1,2,3,4]
x=reduce(lambda a,b:a+b,li)
print(f'sum={x}')
#sum=10

li1=[1,2,3,4]
x=reduce(lambda a,b:a*b,li1)
print(f'product={x}')
#product=24

li2=[6,9,3,0,-5]
x=reduce(lambda a,b:a if a > b else b ,li2)
print(f'max={x}')
#max=9

li3=[8,9,-5,4,6]
x=reduce(lambda a,b:a if a < b else b,li3)
print(f'min={x}')
#min=-5









