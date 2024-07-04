'''def values1(func):
    def inner():
        print("Great work takes time.")
        func()
    return inner
def values2():
    print("Until then work.")
y=values1(values2)
y()


def values1(func):
    def inner():
        print("Great work takes time.")
        func()
    return inner
@values1
def values2():
    print("Until then work.")
values2()'''

def abc(x):
    def inner(a,b):
        print("I am going to divide", a, "and", b)
        if b==0:
            print("cannot return")
            return
        return x(a,b)
    return inner
@abc
def divide(a,b):
    print(a/b)

divide(2,5)
divide(2,0)