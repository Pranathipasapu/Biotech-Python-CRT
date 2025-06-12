#Deletion of Tuple
Tuple=(5,10,15,20,25,30,35,40,50,60,70,80,90,100,110,120,130,140,150,160)
print(Tuple)
del Tuple
#Nested Tuple
nested_tuple=((10,20,30),(40,50,60),(70,80,90))
print(nested_tuple)
print(nested_tuple[0])
print(nested_tuple[1])
print(nested_tuple[2])
#TUPLE CONVERSION
n=int(input("Enter a input:"))
print(f"Before Conversion,The integer value is:{n}")
print(f"After Conversion integer to string :{str(n)}")
print(f"After Conversion integer to float :{float(n)}")
print(f"After Conversion integer to complex :{complex(n)}")
f=float(input("Enter a float value:"))
print(f"Before Conversion,The float value is :{f}")
print(f"After Conversion float to string :{str(f)}")
print(f"After Conversion float to integer :{int(f)}")
print(f"After Conversion float to complex :{complex(f)}")
s=input("Enter a string:")
print(f"Before Conversion,The string is:{s}")
print(f"After Conversion string to integer :{int(s)}")
print(f"After Conversion string to float :{float(s)}")
print(f"After Conversion string to list:{list(s)}")
print(f"After Conversion string to tuple:{tuple(s)}")

