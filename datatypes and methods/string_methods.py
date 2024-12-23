

# word='hello world'
# print(word)
#
# #string concatenation
# a='hello'
# b='hai'
# print(a+' '+b)
#
# #element accessing
# print(word[0])
#
# #string slicing
# print(word[6:11])
#
# print(word[:5])
# print(word[6:])
# print(word[:])
#
# print(word[0:5:2])
#
# print(word[::-1])

#string iteration
# for i in word:
#     print(i)

# user=input("enter the string").strip()
# c=0
# for i in user:
#     c+=1
# print(f'length={c}')
#
# str=input("enter the string").strip()
# c=0
# for i in str:
#     c+=1
# print(f'index={c-1}')

# s=input('enter the string').strip()
# s2=''
# for i in s:
#     if(i !=' ' ):
#         s2+=i
# print(s2)


# str=input('enter the string').strip()
# rev=' '
# for i in str:
#     rev=i+rev
# print(rev)

# str=input('enter the string').strip()
# rev=''
# l=len(str)-1
# for i in range(l,-1,-1):
#     rev+=str[i]
# if(rev==str):
#     print('Palindrome')
# else:
#     print('Not palindrome')

# string=input('enter the string').strip()
# v='aeiouAEIOU'
# c=0
# for i in string:
#     if(i in v ):
#         c+=1
# print(f'count={c}')
# string=input('enter the string').strip()
# v='aeiouAEIOU'
# vow=''
# c=0
# for i in string:
#     if(i in v ):
#         vow+=i
# print(vow)
# #
# greet='Hello World'
# print(type(greet))
#
# # string=str()
# # string_2=greet[1:]
#
# name='Anzil'
# designation='Python django trainer'
# company='Luminar'
# self_intro='I am '+name+' i am working as a '+designation+' at '+company
# self_intro1=f'I am {name} i am working as a {designation} at {company}'
# print(f'self_intro1:{self_intro1}')
# self_intro_2='I am {0} i am working as a {1} at {2}'.format(name,designation,company)
# print(self_intro_2)

# name_1='Jitty S John'
# current_course='Python Django React FullStack Web Development'
# age=26
# completed='MCA'
# place='Adoor'
# self_intro_3='I am {0} {1} 2022 passout.I am {2} year old.I am from {3} and currently studying {4} course.'.format(name_1,completed,age,place,current_course)
# print(self_intro_3)
# self_intro_4='I am {0:s} {1} 2022 passout.I am {2:f} year old.I am from {3:s} and currently studying {4:s} course.'.format(name_1,completed,age,place,current_course)
# print(self_intro_4)
# self_intro_5='I am %s %s 2022 passout.I am %d year old.I am from %s and currently studying %s course.'%(name_1,completed,age,place,current_course)
# print(self_intro_5)
# # name_1[0]='G'
# # print(name_1)
# lst=['h','j','k']
# lst[0]='i'
# print(lst)
#
# str=input('enter string').upper().strip()
# print(str)
# num=5
# chr='abc'
# print(num,chr)
# ch='hello'
# ch2=ch.upper()
# print(ch)
# print(ch2.lower())
#
# name=input('Enter your name')
# name2=name.upper()
# name3=name.lower()
# print(name2)
# print(name3)
#
# name='johndoe'
# nam2=name[0]
# name3=nam2.upper()
# name=name3+name[1:]
# print(name)
#
# n='johndoe'
# formated_name=n[0].upper()+n[1:]
# print(formated_name)
#

# string='abcdefghij'
# text=''
# for i in range(len(string)):
#     if i % 2 != 0:
#         text += string[i].upper()
#     else:
#         text += string[i].lower()
# print(text)


# string='Hello World'
# c1=0
# c2=0

# for i in string:
#     if i.isupper():
#         c1+=1
#     else:
#         c2+=1
# print(f'uppercase={c1} \nlowercase={c2}')
# #
word='hello welcome'
print(word.upper())
print(word.lower())
print(word.title())
print(word.capitalize())
print(word.swapcase())
print(word.find('l'))
print(word.index('o'))
print(word.replace('hello','hai'))
print(word.split())
print(word.count('l'))





# name=input('Enter your name').lstrip()
# if name=='hello':
#    print('welcome')


# string=input('Enter the string').strip()
# alph=0
# num=0
# for i in string:
#     if i.isalpha():
#         alph += 1
#     elif i.isdigit():
#         num += 1
#     else:
#         print('invalid')
# print(f'alphabets:{alph}\nnumbers:{num}')

# word=input('enter the string').strip()
# tem=' '
# for i in word:
#     if i not in tem:
#         tem += i
# print(tem)
#
#
# str= input('Enter input').strip()
# for num,chr in enumerate(str):
#     print(chr,':',num)

# str= input('Enter input').strip()
# str2=''
# for num,chr in enumerate(str):
#     if(num%2==0):
#         str2 += chr.upper()
#     else:
#         str2 += chr.lower()
# print(str2)
