#findall()
#findall( is a function in regex that find all the matches and return them as a list
from re import *
# text='my pincode is 691551 and my phone number is 9845656567'
# pattern='[a-z]{2}'
# match=findall(pattern,text)
# print(match)

# text='I have a cat, and a cute cat'
# pattern='[c][a][t]'
# match=findall(pattern,text)
# print(match)

text="#ffffff and #RRGGBB are color codes"
pattern='#[a-zA-Z]{6}'
match=findall(pattern,text)
print(match)