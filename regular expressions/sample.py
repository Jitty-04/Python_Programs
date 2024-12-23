

# from re import *
# text="usually such patterns are used"
# pattern="us"
# matcher=finditer(pattern,text)
# c=0
# for i in matcher:
#     c+=1
#     print(i.start(),i.group())
# print(f"Total number of '{pattern}' in '{text}' is {c}")

# from re import *
# text="asd456 K123dh"
# #check lower alphabets
# pattern="[a-z]"
# matcher=finditer(pattern,text)
# for i in matcher:
#     print(i.start(),i.group())

# from re import *
# text="asd456 K123dH"
# #check upper alphabets
# pattern="[A-Z]"
# matcher=finditer(pattern,text)
# for i in matcher:
#     print(i.start(),i.group())

# from re import *
# text="asd456 K123dH"
# #check numbers
# pattern="[0-9]"
# matcher=finditer(pattern,text)
# for i in matcher:
#     print(i.start(),i.group())

# from re import *
#
# text = "asd456 K123dH"
# # check lower & upper
# pattern = "[a-zA-Z]"
# matcher = finditer(pattern, text)
# for i in matcher:
#     print(i.start(), i.group())

from re import *
#
# text = "asd45@6 K1$23dH"
# # check special character ^exclude all pattern after ^
# pattern = "[^a-zA-Z0-9 ]" #whitespace
# matcher = finditer(pattern, text)
# for i in matcher:
#     print(i.start(), i.group())

#fullmatch

# from re import *
# word="hello"
# pattern='[a-z]+'
# match=fullmatch(pattern,word)
# if match:
#     print('match is found')
# else:
#     print('match not found')

#name start upper rest lower
# name=input('enter name').strip()
# pattern='[A-Z][a-z]+'
# match=fullmatch(pattern,name)
# if match:
#     print('name is valid')
# else:
#     print('name is  invalid')

#name start A,B or C rest lower
# name=input('enter name').strip()
# pattern='[ABC][a-z]*'
# match=fullmatch(pattern,name)
# if match:
#     print('name is valid')
# else:
#     print('name is  invalid')

#limit:5
# word=input('enter the word').strip()
# pattern='([A-Z]){5}|([a-z]{5})'
# match=fullmatch(pattern,word)
# if match:
#     print('valid')
# else:
#     print('invalid')

#name start with caps
#rest lower
#limit :(5,8)
# name=input('enter name').strip()
# pattern="[A-Z][a-z]{4,7}"
# match=fullmatch(pattern,name)
# if match:
#     print('valid')
# else:
#     print('invalid')

#name23
#limit:2
#anshya23 ,anshya(valid)
# anshya1(invalid)

# name=input('enter the name').strip()
# pattern='([a-z]+)|[a-z]+[0-9]{2}'
# match=fullmatch(pattern,name)
# if match:
#     print('valid')
# else:
#     print('invalid')

#validate the postal code
#write a regex rule to validate a 5 digit US postal code
#eg:12345(valid) 123a,123-45

# code=(input("enter the postal code")).strip()
# pattern=r'\d{5}'
# match=fullmatch(pattern,code)
# if match:
#     print('valid')
# else:
#     print('not valid')

#write regex rule to validate the phone number
# 9 8 7 6
#limit 10

# number=input('enter the number').strip()
# pattern=r'[6-9]\d{9}'
# match=fullmatch(pattern,number)
# if match:
#     print('valid')
# else:
#     print('invalid')

from re import *
# number=input('enter the number').strip()
# pattern=r'\+91[6-9][0-9]{9}'
# match=fullmatch(pattern,number)
# if match:
#     print('valid')
# else:
#     print('invalid')

# month=input('enter the month').strip()
# pattern='0[1-9]|1[0-2]'
# match=fullmatch(pattern,month)
# if match:
#     print('valid')
# else:
#     print('invalid')

# year=input('enter the year').strip()
# pattern='(19[0-9]{2})|(20[0-9]{2})'
# match=fullmatch(pattern,year)
# if match:
#     print('valid')
# else:
#     print('invalid')

# day=input('enter the day').strip()
# pattern='(0[1-9])|(1[0-9])|(2[0-9])|(3[0-1])'
# match=fullmatch(pattern,day)
# if match:
#     print('valid')
# else:
#     print('invalid')

date=input('enter the date').strip()
pattern=r'^(19|20)\d{2}[-](0[1-9]|1[0-2])[-](0[1-9]|[12]\d|3[01])|^(19|20)\d{2}[/](0[1-9]|1[0-2])[/](0[1-9]|[12]\d|3[01])'

match=fullmatch(pattern,date)
if match:
    print('valid')
else:
    print('invalid')










