def integers(num):
    if num>0:    
        print(f"Positive number={num}")
    elif num<0:
        print(f"Negative number={num}")
    else:
        print("Zero")
integers(num=int(input("Enter the input:")))
