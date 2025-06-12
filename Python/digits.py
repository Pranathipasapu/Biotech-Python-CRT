i=int(input())
if(i>=0 and i<=9):
    print("Single digit")
if(i<=99 and i>=10):
    print("Two digits")
if(i<=999 and i>=99):
    print("Three digits")
if(i>999):
    print("More than three digits")
