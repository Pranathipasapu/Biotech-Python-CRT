#MULTI-LEVEEL INHERITANCE
class grandfather():
    def show(self):
        print("This is a granfather class")
class father(grandfather):
    def show1(self):
        print("This is the father class")
class son(father):
    def show2(self):
        print("This is son class")
s1=son()
s1.show()
s1.show1()
s1.show2()
print()

#MULTIPLE INHERITANCE
class dance:
    def dancing(self):
        print("I can dance")
class fly:
    def flying(self):
        print("I can fly also")
class peacock(dance,fly):
    def sound(self):
        print("I had a good sound too")
p1=peacock()
p1.dancing()
p1.flying()
p1.sound()
print()
#HIERARCHIAL INHERITANCE
class shape:
    def area(self):
        print("calculate area:")
class circle(shape):
    def circlearea(self,radius):
        print("area of circle",3.14*radius*radius)
class square(shape):
    def squarearea(self,side):
        print("area of square=",side*side)
c1=circle()
c1.area()
c1.circlearea(5)
s1=square()
s1.area()
s1.squarearea(5)
print()

#OVERRIDING
class bank:
    def getroi(self):
        return 10
class sbi(bank):
    def getroi(self):
        return 8
class icici(bank):
    def getroi(self):
        return 9
b1=bank()
print(b1.getroi())
s1=sbi()
print(s1.getroi())
i1=icici()
print(i1.getroi())
