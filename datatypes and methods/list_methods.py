# list=[1,2,'a','b','c']
# print(list)
from itertools import count

# element accesing

# print(list[2])

# slicing

# print(list[0:])
# print(list[:])
# print(list[2:5])
# print(list[::-1])
# print(list[0:5:2])

# list iteration
# for i in list:
#     print(i)

#
# li=eval(input('enter the data'))
# print(li)
# c=0
# for i in li:
#     c+=1
# print(f'length of list={c}')


# data=eval(input('Enter data'))
# print(data)
# s=0
# for i in data:
#     s += i
# print(f'sum={s}')
#
l=eval(input('enter the data'))
s=[]
for i in l:
    if i not in s:
        s += [i]
print(s)
#
# list=eval(input('enter data'))
# print(list)
# rev=[]
# l=len(list)-1
# for i in range(l,-1,-1):
#     rev+=[list[i]]
# print(rev)

# p=eval(input('Enter data'))
# reverse=' '
# tem=[]
# r=[]
# length=len(p)
# # print(length)
# for i in range(0,length):
#     tem=p[i]
#     # print(tem)
#     l=len(tem)-1 #hello
#     for k in range(l,-1,-1):
#           reverse += tem[k]
#     # print(reverse)
#     r +=[reverse]
#     reverse=' '
#
# print(r)

# li=eval(input('enter data'))
# rev=[]
# for i in li: #hello
#     d=""
#     for j in i: # h e l l o       hai
#         d=j+d #o l l e h          iah
#     rev+=[d] #olleh               iah
# print(rev)



# li=eval(input('enter data'))
# max=li[0]
# for i in li:
#   if i > max:
#       max=i
# print(f'max:{max}')

# l=eval(input('enter number'))
# f=1
# t=[]
# for n in l:
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     t += [f]
# print(t)


# num=eval(input('enter numbers'))
# s=[]
# for n in num:
#     rev=0
#     while(n>0):
#         r=n%10
#         rev=rev*10+r
#         n=n//10
#     s += [rev]
# print(s)







#
# li=eval(input('enter data'))
# min=li[0]
# for i in li:
#   if i < min:
#       min=i
# print(f'min:{min}')

li=['a','b','c']
li.append('d')
print(li)
li.insert(0,'hello')
print(li)
li.extend([1,2,3])
print(li)
print(li.index('hello'))
li.pop()
print(li)
li.pop( 2)
print(li)
li.remove('d')
print(li)
li.reverse()
print(li)
li2=[1,7,9,0]
# li2.sort()
li2.sort(reverse=True)
print(li2)
li3=['a','A','b','B']
li3.sort()
li4=['a','a','b',1]
print(li4.count('a'))
li5=['a',4,5]
li5.clear()
print(li5)








