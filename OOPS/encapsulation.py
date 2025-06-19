class base:
    def __init__(self):
        self.__a=32
        print(self.__a)
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self.__a+2)
b1=base()

###
class Base:
    def __init__(self):
        self._a=32
        print(self._a)
class Derived(Base):
    def __init__(self):
        super().__init__()
        print(self._a+2)
class Derived1(Derived):
    def __init__(self):
        super.__init__(self)
        print(self._a+3)
a1=Derived1
###STATIC METHOD-1
class mathematics:
    def addnumber(x,y):
        return x+y
m=staticmethod(mathematics.addnumber)
print(m(4,44))
###2
class mathematics:
    @staticmethod
    def addnumbers(x,y):
        return x+y
print(mathematics.addnumbers(4,44))
