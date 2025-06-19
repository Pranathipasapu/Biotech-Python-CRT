class Father:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
class Son(Father):
    def __init__(self,name):
        self.name=name
    def show1(self):
        print(self.name)
x=Father('Nagarjuna')
x.show()
y=Son('Akhil')
y.show1()
y.show()

