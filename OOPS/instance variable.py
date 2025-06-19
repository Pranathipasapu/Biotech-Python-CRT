#WITH CONSTRUCTOR
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person('Kiran',40)
p2=person('Sandeep',41)
print(p1.name,p1.age)
print(p2.name,p2.age)

#WITHOUT CONSTRUCTOR
class person:
    name=''
    age=''
p1=person()
p1.name="Kiran"
p1.age="40"
p2=person()
p2.name="Sandeep"
p2.age="41"
print(p1.name,p1.age)
print(p2.name,p2.age)




