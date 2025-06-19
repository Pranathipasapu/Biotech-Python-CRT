#write a program to perform the sum of individual adigits of the given positive integer number n till the result is of single digit number
n=int(input())
sd=0
while n!=0:
    r=n%10
    sd+=r
    n=n//10
    if(n==0 and sd>0):
        n=sd
        sd=0
print(sd)
