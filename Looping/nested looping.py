# for i in range(5): #0 1 2 3 4
#     for j in range(5): #0 1 2 3 4
#         print('*',end=' ' )
#     print()
#
# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i}*{j} = {i*j}')
#     print()

# pattern printing
# for i in range(3): # 0 ,1 ,2
#      for j in range(i+1): #1,2,3
#          print('*',end=' ')
#      print()

# for i in range(6): # 0 ,1 ,2,3,4,5
#      for j in range(i+1): #1,2,3,4,5,6
#          print('*',end=' ')
#      print()

#
# for i in range(3,0,-1):
#     for j in range(i):
#         print('*',end=' ')
#     print()
#
# for i in range(5):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(4,0,-1):
#     for j in range(i):
#         print('*',end=' ')
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print(i+1,end=' ')
#     print()
#
# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end=' ')
#     print()
# for i in range(1,5):
#     for j in range(i):
#         print(j+1,end=' ')
#     print()
# for i in range(4):
#     for j in range(i+1):
#         print(i,end=' ')
#
# for i in range(1,4):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()

# for i in range(1,5):
#     for j in range(i):
#         print(j+1,end=' ')
#     print()
# for i in range(3,0,-1):
#     for j in range(i):
#         print(j+1,end=' ')
#     print()

# n=5
# for i in range(n):
#     if(i==0 or i==n-1):
#         print('*' * n)
#     else:
#         print('*'+ ' ' *(n-2)+ '*')

#
# for i in range(3):
#     for k in range(2-i):
#         print(' ',end='')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
#
# for i in range(5):
#     for k in range(i):
#         print(' ',end='')
#     for j in range(5-i):
#         print('*',end=' ')
#     print()
#
#
# for i in range(6):
#     for k in range(5-i):
#         print(' ',end='')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(5):
#     for k in range(i+1):
#         print(' ',end='')
#     for j in range(5-i):
#         print('*',end=' ')
#     print()

#
for i in range(1,7):
    for k in range(7-i):
        print(' ',end='')
    for j in range(i):
        print(i,end=' ')
    print()
for i in range(5):
    for k in range(i+2):
        print(' ',end='')
    for j in range(5-i):
        print(5-i,end=' ')
    print()
#
for i in range(65,68):
    for j in range(65,i+1):
        print(chr(i),end=' ')
    print()
for i in range(97,103):
    for j in range(97,i+1):
        print(chr(i),end=' ')
    print()