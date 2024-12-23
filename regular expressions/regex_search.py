#what is search in regex?
#it returns a match object anywhere in a string
#it returns only the first match

from re import *
#
# text=('my phone number is 9878787676')
# pattern='[0-9]'
# match=search(pattern,text)
# if match:
#     print(match.group(),match.start())



# text='Apples are amazing and abundant'
# pattern=r'[A]\w*'
# match=search(pattern,text)
# if match:
#     print(match.group())

# string='Contact me at jitty12@yahoo.com or jitty@gmail.com'
# pattern=r'\w+\@[y][a][h][o][o][.][c][o][m]'
# match=search(pattern,string)
# if match:
#     print(match.group())

text="Today's date is  16/11/2024"
pattern='(0[1-9]|1[0-9]|2[0-9]|3[0-1])[/](0[1-9]|1[0-2])[/](19|20[0-9]{2})'
match=search(pattern,text)
if match:
    print(match.group())


