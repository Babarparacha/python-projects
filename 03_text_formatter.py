
text=input("enter some text:")
print("1-upper case")
print("2-lower case")
print("3-title case")
print("4-sentence case")
choice=int(input('choose a format(1-4) :'))

if choice==1:
    print(text.upper())
elif choice==2:
    print(text.lower())
elif choice==3:
    print(text.title())
elif choice==4:
 print(text.capitalize())   