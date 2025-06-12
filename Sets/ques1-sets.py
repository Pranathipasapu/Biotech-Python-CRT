string=input("Enter the input:")
A=0
T=0
G=0
C=0
for i in string:
    if i=='A':
        A+=1
    elif i=='T':
        T+=1
    elif i=='C':
        C+=1
    elif i=='G':
        G+=1
    else:
        print("Invalid Outputt")
My_dict={
    'A':A,
    'T':T,
    'C':C,
    'G':G,
    }
print(My_dict)
