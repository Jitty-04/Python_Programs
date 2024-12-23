import random

#generate random integer between 10 and 20
print(random.randint(10,20))

#generate a random float between 5.5 and 10.5
print(random.uniform(5.5,10.5))

#select a random element from a list
items=['apple','mango','banana']
print(random.choice(items))

#select 2 random elements from a list
print(random.sample(items,2))

#shuffle a list in place
random.shuffle(items)
print(items)

