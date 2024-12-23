d={'a':1,'b':2,'c':3}
##keys()
# print(d.keys())
# #values()
# print(d.values())
# #items()
# print(d.items())
# #get()
print(d.get('a'))
print(d.get('d'))
# print(d.get('d','not found'))
# #pop()
# d2={1:'a',2:'b'}
# print(d2.pop(1))
# print(d2)
# print(d2.pop(3,'not exist'))
# #popitem()
d3={'a':1,'b':2,'c':3}
d3.popitem()
print(d3)
# #update()
# d3.update({'c':6})
# print(d3)
# d3['b']=4
# print(d3)
# #change key
# d3['d']=d3.pop('b')
# print(d3)
# for i in d3:
#     print(i)
# for i in d3.values():
#     print(i)
# for i in d3.items():
#     print(i)
#
# for i,j in d3.items():
#     print(i,j)
from collections import defaultdict

string=input('enter the input')
dic={}
for i in string:
       dic[i]=string.count(i)
print(dic)
#
str=input('enter string')
dic={}
for i in str:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
#
data=eval(input('enter data'))
# print(data)
li=[]
dic={}

for i in data:
    c=0
    for j in i:
        c+=1
    l=c
    dic[i]=l

li=dic
print(li)

# num=eval(input('enter numbers'))
# l=[]
# d={}
# for i in num:
#     if i%2==0:
#         d[i]='even'
#     else:
#         d[i]='odd'
# l=d
# print(l)

