str=input("Enter the string:")
digit_count=0
vowel_count=0
special_char=0
for ch in str.lower():
    if ch.isdigit():
        digit_count+=1
    elif ch.isalpha():
        if ch in ['a','e','i','o','u']:
            vowel_count+=1
    else:
        special_char+=1
print(f"Digit count:{digit_count}")
print(f"Vowel count:{vowel_count}")
print(f"Special char count:{special_char}")
       
      
