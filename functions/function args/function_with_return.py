# def add(a,b):
#     return a+b
# x=(add(1,2))
# print(x)
#
# def add(a,b):
#     print(a+b)
# add(1,2)



# def oddeven(a):
#     if a %2 ==0:
#         return 'even'
#     else:
#         return 'odd'
# print(oddeven(3))
# print(oddeven(2))

# def large(a,b,c):
#     if a>b:
#         if a>c:
#             return a
#     elif b>c:
#         return b
#     else:
#         return c
# print(f'largest={large(2,5,3)}')


# def disarium(num):
#     l=len(str(num))
#     n=num
#     s=0
#     while(num!=0):
#         r=num%10
#         s+=r**l
#         num=num//10
#         l-=1
#     if s==n:
#         return 'dissarium'
#     else:
#         return 'not dissarium'
# print(disarium(175))
# print(disarium(150))


# def list_elements_square(li):
#     li1=[]
#     for i in li:
#         li1+=[i**2]
#     return li1
# print(list_elements_square([2,4,6]))




# def list_element_reverse(li2):
#     li3=[]
#     for i in li2:
#         r=0
#         rev=0
#         while(i!=0):
#             r=i%10
#             rev=rev*10+r
#             i=i//10
#         li3+=[rev]
#     return li3
# print(list_element_reverse([345,789,678]))

# def unique_chars(s):
#     li=[]
#     for i in s:
#         c=0
#         c=s.count(i)
#         if c==1:
#             li+=[i]
#     return li
# print(unique_chars('common'))


# def string_reverse(*str):
#     dic={}
#     for i in str:
#         rev=''
#         for j in i:
#             rev=j+rev
#             dic[i]=rev
#     return dic
# print(string_reverse('hello','hai'))


def quad(a,b,c):
    d = (b ** 2 - 4 * a * c) ** 0.5
    x1 = (-b + d) / 2 * a
    x2 = (-b - d) / 2 * a
    return x1,x2
x=(quad(1,5,6))
print(f'x1={x[0]}\nx2={x[1]}')


# def even(li):
#     even=[]
#     for i in li:
#         if i % 2==0:
#             even+=[i]
#     return even
# print(even([3,7,2,4,1]))

























