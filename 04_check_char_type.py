
char=input('Enter a single character to check type:')

if char.isalpha():
    print("this is a letter")
elif char.isdigit():
    print("this is a digit")
else:
    print("this is a special letter")