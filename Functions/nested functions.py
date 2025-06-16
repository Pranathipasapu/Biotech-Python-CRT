def Eat():
    def WashHands():
        print("Wash your hands")
    def ServeFood():
        print("Serve the food")
    ServeFood()
    WashHands()
    print("Enjoy your meal")
    print("Wash your hands")
Eat()

#Function
def Hello():
    print("Hello World")
Hello()
print(Hello())

#
def disp():
    def show():
        return "Show Function"
    print("Disp Function")
    return show
r_sh=disp()
print(r_sh())

#Demo Func
def display(a):
    print("a:",a())
def demo():
    print("Hey.....!I'm a demo function...!")
display(demo)

def Print(a,b):
    print(f"a:",a)
    print(f"b:",b)
#Print(a,b) #Parameter
Print(10,20)
#Positional Arguement
def pw(x,y):
    z=x**y
    print(z)
pw(5,2)
#Arguements
def add(x,y):#Formal arguement
    c=x+y
    print(c)
add(10,20)
#Keyword Arguements
def show(name,age):
    print(name,age)
show(name="Kumar",age=62)
#Default Arguement
def show(name,age=27):
    print(name,age)
show(name="Raam",age=62)
#variable length arguement
def add(*num):
    z=num[0]+num[1]+num[2]
    print(z)
add(5,2,4)
#Keyword Variable length Arguements
def add(**num):
    z=num['a']+num['b']+num['c']
    print(z)
add(a=5,b=2,c=4)
