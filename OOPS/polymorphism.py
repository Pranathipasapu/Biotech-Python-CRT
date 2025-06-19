#POLYMORPHISM
class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,o):
        return self.a+o.a
ob1=A(1)
ob2=A(2)
ob3=A("Geeks")
ob4=A("For")
print()

###Resolution order method
class A:
    def myname(self):
        print("I am a classA")
class B(A):
    def myname(self):
        print("I am a class B")
class C(A):
    def myname(self):
        print("I am a class C")
class D(C,B):
    pass
d=D()
d.myname()
print(D.__mro__)
