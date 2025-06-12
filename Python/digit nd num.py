n=int(input())
if(n>=-9 and n<=9):
    print(f"{n} is digit")
else:
    print(f"{n} is number")
#Ternary Operator
r="Digit" if(n>=-9 and n<=9) else "Number"
print(f"{n} is {res}")
