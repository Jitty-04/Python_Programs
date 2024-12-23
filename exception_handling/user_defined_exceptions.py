#negative:Negative Error
#Zero    :Zero Error

class NegativeError(Exception):
    def __init__(self,message='Negative Error'):        #pass
        super().__init__(message)

class ZeroError(Exception):
    def __init__(self,message='Zero Error'):            #pass
        super().__init__(message)

try:
    num=int(input('enter the number'))
    if num==0:
        raise ZeroError
    elif num<0:
        raise NegativeError
except ZeroError as err:                        #except ZeroError:
    print(err)                                           #print("zero error occured")
except NegativeError as err:
    print(err)


else:
    print("positive number")

