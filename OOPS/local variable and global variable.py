#LOCAL VARIABLE-inside the function
def a1():
    a=5
    c=a+b
    print(c)
    print(a)
    print(id(a))
def a2():
    a=10
    print(a)
    print(id(a))
#GLOBAL VARIABLE-outside the function
b=15
print(b)
print(id(b))
a1()
a2()
