#Recursion in python is when a function calls itself to solve a problem by breaking it down into smaller,more managable sub problems.
#The recursion continues until a base case is reached,which stops the recursion


#Simple recursive function that calculates the factorial of a number

def factorial(num):
    if num==0:    #basecase if n is 0 factorial is 1(condition under which recursion ends)
        return 1
    else:
        return num*factorial(num-1) #recursivecase num!= num*(num-1)! (function calls itself with a modified argument moving toward base case)
print(factorial(6))


#Fibonacci Series using recursion

def fibonacci(num):
    #base cases:fibonacci(0) is 0 and fibonacci(1) is 1
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2) #recursive case
print(fibonacci(8))



#Sum of List of numbers
def sum(list):
    if len(list)==0: #base case
        return 0
    else:
        return list[0]+sum(list[1:])
print(sum([1,2,3,4]))

#Power of a Number
def power(x,num):
    if num==0:    #basecase
        return 1
    else:
        return x*power(x,num-1)
print(power(6,2))
print(power(3,4))







