#Represent the name of the customer and the number of items purchased by the customer in the store using a class.
#As per the number of items read the prices and calculate the total price,If the total price is >200 rupees provide a discount of 20% if not no discount
class store:
    def __init__(self,name,noofitems):
        self.name=name
        self.noofitems=noofitems
    def calculation(self):
        x=self.noofitems
        tp=0
        for i in range(x):
            p=int(input())
            tp+=p
        return tp
name=input("Enter the Name:")
noofitems=int(input("Enter the No of Items:"))
c1=store(name,noofitems)
tp=c1.calculation()
print("Total:",tp)
if(tp>=200):
    print("After Discount",tp-tp*0.2)
else:
    print(tp)

#SECOND-METHOD
class customer:
    def __init__(self,name,item1,item2,item3,item4):
        self.name=name
        self.item1=item1
        self.item2=item2
        self.item3=item3
        self.item4=item4
    def calculation(self):
        print(self.name)
        tot=self.item1+self.item2+self.item3+self.item4
        print(tot)
        if(tot>200):
            t=tot-tot*(20/100)
            print(t)
        else:
            t=tot
s1=customer("Kiran",80,50,50,70)
s1.calculation()
print()
    
