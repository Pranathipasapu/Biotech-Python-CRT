password = input("Enter the password: ")
alphabets_count = 0
digits_count = 0
spl_count = 0
spl_chars = '!@#$%^&*'
for ch in password:
    if ch.isalpha():
        alphabets_count += 1
    elif ch.isdigit():
        digits_count += 1
    elif ch in spl_chars:  
        spl_count += 1
if alphabets_count!= 0 and digits_count!= 0 and spl_count!= 0:
    print("VALID PASSWORD")
else:
    print("INVALID PASSWORD")

        
        
