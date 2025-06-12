list=[10,20,30,40,50,60,70]
print(list)
print(list[::])
print(list[1:4:1])   
print(list[::2])
print(list[::-1])

size=int(input("Enter the size of the list:"))
list=[]
for i in range(size):
    temp=int(input(f"Enter the integer value at {i}:"))
    list.append(temp)
print(f"User Entered list:{list}")
print(list[::-1])

