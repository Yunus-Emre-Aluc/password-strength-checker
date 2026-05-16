import sys

password=input("Enter a strong password: ")

missing=[]

digit_count=0
uppercase_count=0
lowercase_count=0
special_char_count=0
score=0

if " " in password:
    print("Password cannot contain spaces")
    sys.exit()

for char in password:
    if char.isupper():
        uppercase_count+=1
    elif char.isdigit():
        digit_count+=1
    elif char.islower():
        lowercase_count+=1
    elif not char.isalnum():
        special_char_count+=1

if len(password)>=10:
    score+=1
else:
    missing.append("Must be at least 10 characters long")
if uppercase_count>=3:
    score+=1
else:
    missing.append("Must contain at least 3 uppercase letters")
if digit_count>=3:
    score+=1
else:
    missing.append("Must contain at least 3 digits")
if lowercase_count>=3:
    score+=1
else:
    missing.append("Must contain at least 3 lowercase letters")
if special_char_count>=1:
    score+=1
else:
    missing.append("Must contain at least 1 special character")


for miss in missing:
    print(miss)

if score<=1:
    print("WEAK password...")
elif score<=3:
    print("MEDIUM password...")
elif score<=4:
    print("STRONG password...")
else:
    print("Password meets all criteria! VERY STRONG password...")