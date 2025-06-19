#CLASS CREATION
class person:
    age=36#Static variable
    name='Kiran'
#OBJECT CREATION
p1=person()
#CONNECTION-CLASS&OBJECT
print(p1.age,p1.name)

p2=person()
print(p2.age)
print(person.age)
