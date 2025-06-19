#a. Represent name, rno, 3 subjects marks of a student using a class.
#b. The 3 subjects are maths, physics, chemistry
#c.First verify whether the student is pass or fail,if passed in all the 3 subjects then calculate and print the:
#1. total 2.average 3.admission is confirmed in engineering or not
#Condition for admission confirmation in engineering: out of 3 subjects in any 2 subjects the score should be >75 otherwise print a message as fail

class student:
    def __init__(self,name,rno,math,phy,chem):
        self.name=name
        self.rno=rno
        self.math=math
        self.phy=phy
        self.chem=chem
    def calculation(self):
        if(self.math>=40 and self.phy>=40 and self.chem>=40):
            total=self.math+self.phy+self.chem
            avg=total/3
            print(total)
            print(avg)
            if(self.math>75 and self.phy>75) or (self.phy>75 and self.chem>75) or (self.math>75 and self.chem>75):
                print("Admission is confirmed")
            else:
                print("Admisssion not confirmed")
        else:
            print("Fail")
s1=student("Kiran",501,74,85,85)
s1.calculation()
