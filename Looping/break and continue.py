# for i in range(1,10):
#     if(i==5):
#      continue
#     else:
#         print(i)
# for i in range(1,101):
#     if(i%2==0 and i%3!=0):
#         continue
#     else:
#         print(i)
#
# for i in range(1,101):
#     if(i%3==0):
#         continue
#     else:
#         print(i)f
# for i in range(1,10):
#     print(i)
# else:
#     print('completed')
num=int(input('enter the number'))
if(num<=1):
    print('Not prime')
else:
  for i in range(2,num):
      if(num%i==0):
          print('Not prime')
          break
  else:
      print('prime')


#7 - 7<=1 false
#  enter for loop range(2,6)
#  i=2,3,4,5,6
#  check if 7%(2,3,4,5,6)==0 condition false
#   print else body ie,prime


# 8-8<=1 false
# enter for loop range(2,7)
# i=2,3,4,5,6,7
# check if 8%2 ==0 true
# print if body ie,not prime
#break from loop

