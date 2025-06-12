num=int(input("Enter the number:"))
even_list=[]
odd_list=[]
for i in range(1,num+1,2):
    odd_list.append(i)
for i in range(2,num+1,2):
    even_list.append(i)
print("Even List:",even_list)
print("Odd List:",odd_list)
