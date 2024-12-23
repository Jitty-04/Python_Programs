# while True:
#     print('hello')
from math import factorial

# i=1
# while(i<=10):
#     print(i)
#     i+=1

# i=0
# while(i<=50):
#     print(i,end=' ')
#     i+=1

# i=2
# while(i<=20):
#     if(i%2==0):
#         print(i)
#     i+=1
#
# print()

# i=1
# while(i<=9):
#     if(i%2!=0):
#         print(i)
#     i+=1


# i=1
# sum=0
# while(i<=10):
#     sum+=i
#     i+=1
# print(f'sum={sum}')

# i=1
# p1=1
# p2=1
# while(i<=10):
#     if(i%2==0):
#         p1*=i
#     else:
#        p2*=i
#     i+=1
#
# print(f'Product of even nos={p1}')
# print(f'Product of odd nos={p2}')

# c1=0
# c2=0
# n1=int(input('Enter initial range'))
# n2=int(input('Enter final range'))
# i=n1
# while(i<=n2):
#     if(i%2==0):
#         c1+=1
#     else:
#         c2+=1
#     i+=1
# print(f'Count of even nos: {c1}')
# print((f'count of odd nos: {c2}'))

# i=10
# while(i>=1):
#     print(i)
#     i-=1

# n1=int(input("Enter the number"))
# n2=int(input('enter the range'))
# i=1
# while(i<=n2):
#     print(f'{n1}*{i}={n1*i}')
#     i+=1
#
# i=11
# while(i>=2):
#     if(i%2==0):
#         print(i)
#     i-=1
#
# i=1
# while(i<=10):
#     print(f'{i}:{i**2}')
#     i+=1


# n1=int(input('Enter the number'))
# i=1
# f=1
# while(i<=n1):
#     f*=i
#     i+=1
# print(f'factorial={f}')


# i=1
# while(i<=100):
#     if(i%11==0):
#         i+=1 # while skip iteration specifies
#         continue
#     print(i)
#     i+=1

# n=int(input('Enter the range'))
# i=3
# s=0
# while(i<=n):
#     if(i%3==0):
#         s+=i
#     i+=1
# print(s)

# n1=int(input('enter the number'))
# c=0
# i=2
# while(i<=n1):
#     if(i%2==0):
#         c+=1
#     i+=1
# print(c)

# n=int(input('enter the number'))
# s=0
# rem=0
# while(n!=0):
#     rem=n%10
#     s+=rem
#     n//=10
# print(f'sum={s}')

# num=int(input('enter the number'))
# rev=0
# rem=0
# while(num!=0):
#     rem=num%10
#     rev=rev*10+rem
#     num//=10
# print(rev)
#
# num=int(input('enter the number'))
# rev=0
# rem=0
# p=num
# while(num!=0):
#     rem=num%10
#     rev=rev*10+rem
#     num//=10
# if(p==rev):
#     print('Palindrme')
# else:
#     print('Not palindrome')

# n=int(input('enter the number'))
# p=n
# s=0
# while(n!=0):
#     r=n%10
#     s+=r
#     n//=10
# if(p%s==0):
#     print('Harshad number')
# else:
#     print('Not Harshad')

# n=int(input('enter the number'))#175
# l=len(str(n)) #3
# p=n
# s=0
# while(n!=0):
#     r=n%10 #5 #7 #1
#     s+=r**l #s+=5**3 125, s+=7**2 125+49 =174,s+=1**1 174+1=175
#     n//=10 #17 #1 #0
#     l-=1 #2 #1 #0
# if(s==p):
#     print('Disserium number')
# else:
#     print('Not disserium number')

# num=int(input('Enter the number')) #1634
# l=len(str(num)) #4
# tem=num #1634
# s=0
# while(num!=0):
#     r=num%10 #4            3                    6                 1                  0
#     s+=r**l #s=4**4 :1=256,  s=256+(3**4) :337,s=337+(6**4)=1633,s=1633+(1**4)=1634,
#     num//=10 #163 16 1 0
# if(s==tem): #1634==1634
#     print('Number is amstrong')
# else:
#     print('Number is not amstrong')

# num=int(input('enter the number'))
c1=0
c2=0
while(1):
    num=int(input("enter the number"))
    if(num==0):
        break
    elif(num%2==0):
        c1+=1
    else:
        c2+=1
print(f'total even={c1}')
print(f'total odd={c2}')






















