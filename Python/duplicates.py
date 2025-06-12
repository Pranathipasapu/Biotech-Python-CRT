size=int(input("Enter the size of list:"))
list=[]
unique_list=[]
for i in range(size):
    temp=int(input(f"Enter the integer value at {i} index position:"))
    list.append(temp)
print(f"User Entered list:{list}")
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(f"unique list:{unique_list}")
