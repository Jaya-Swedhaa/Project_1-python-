x= lambda a,b,c : a+b+c
print(x(4,5,6))

def myfunc(n):
    return lambda a: a*n
x=myfunc(2)
print(x(3))