#positional arguments
# def multiply(a,b):
#     print(a*b)
# multiply(3,6)

#default argument
# def add(a,b,c=0):
#     print(a+b+c)
# add(1,2)
# add(1,2,3)

# def product(a,b=0,c=2,d=1):
#     print(a*b*c*d)
# product(1,2,3,4)
# product(1,2,3)
# product(1,2)

# def values(*args):
#     print(args)
# values(1,4,6)
# values(1,6,8,9,0,5)




# def add(*add):
#     s=0
#     for i in add:
#         s+=i
#     print(s)
# add(1,2,3)
# add(1,2,3,4)


# def multiply(*mul):
#     p=1
#     for i in mul:
#         p*=i
#     print(p)
# multiply(2,3)
# multiply(4,5,3,2)

# def minvalue(*min):
#     minimum=min[0]
#     for i in min:
#         if i < minimum:
#             minimum=i
#     print(f'minimum={minimum}')
# minvalue(1,4,6,2)
# minvalue(2,3,-9)


# def maxvalue(*max):
#     maximum=max[0]
#     for i in max:
#         if i > maximum:
#             maximum=i
#     print(f'maximum={maximum}')
# maxvalue(5,7,9,2)
# maxvalue(2,3,10)


#keyword arguments
# def add(a,b):
#     print(a+b)
# add(b=2,a=1)


def person(name,email,phone,address):
    print(name,email,phone,address)
person(name='Jitty',email='jitty@123',phone=989897689,address='adoor')



# arbitary keyword
def values(**kwargs):
    print(kwargs)
values(name='Jitty',email='jitty@123')
values(id='1',name='Jitty',department='MCA')


# list as arg
def list_sum(li):
    print(li)
list_sum([1,2,3,4])















