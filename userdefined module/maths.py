#function with return
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

def product(*args):
    product=1
    for i in args:
        product*=i
    return product

def minvalue(*min):
    minimum=min[0]
    for i in min:
        if i < minimum:
            minimum=i
    return minimum

def maxvalue(*max):
    maximum=max[0]
    for i in max:
        if i > maximum:
            maximum=i
    return maximum


