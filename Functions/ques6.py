def palindrome(num):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if(count==2):
        return "Prime Palindrome number" if n=n[::-1] else "Not a Prime Palindrome number"
palindrome(n)
