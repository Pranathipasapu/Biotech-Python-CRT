size=int(input("Enter the range of list:"))
num=[]
for i in range(size):
    value=int(input("Enter the number at {i} index:"))
    num.append(value)
print("Original List:{num}")
for i in range(size):
    if(num[i]<0):
         num[i]=0
    if(num[i]%3==0):
         print(num[i])
         
         
         
         
