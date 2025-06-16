#METHOD-1
def is_primenumber(num):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if(count==2):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
is_primenumber(num=int(input("Enter the input:")))
#METHOD-2
def is_primenumber(num):
    count=0
    for i in range(2,num//2+1):
        if(num%i==0):
            count+=1
    if(count==0):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
is_primenumber(num=int(input("Enter the input:")))
