#Printing
class person():
    def __init__(self,name,age): #Parametrized constructor
        self.name=name
        self.age=age
    def printing(self):
        print(self.name,self.age)
    def decide(self):
        if (self.age)>18:
            print("Major")
        else:
            print("Minor")
    def uppercaseconversion(self):
        print(self.name.upper())
    def length(self):
        print(len(self.name))
p1=person('Kiran',40)
p2=person('Sandeep',41)
p1.printing()
p2.printing()
p1.decide()
p2.decide()
p1.uppercaseconversion()
p2.uppercaseconversion()
p1.length()
p2.length()

#Non-Parametrized Constructor
class person():
    c=0
    def __init__(self):
        person.c+=1
p1=person()
print(p1.c)
p2=person()
print(person.c)
p3=person()
print(person.c)

