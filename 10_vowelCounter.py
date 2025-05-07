# there are two solution for that 
# while True:
#     text=input("enter some text (or quit):")
#     if text.lower()=="quit":
#         print('goodbye')
#         break
#     vowelCount=0
#     for letter in text.lower():
#         if letter in ['a','e','i','o','u']:
#             vowelCount+=1
#     print(f"that text has {vowelCount} vowels!")      

 # advace sytax for the samew example
while True:    
 text=input("enter some text (or quit):")
 if text.lower()=="quit":
    print('goodbye')
    break
 vowels=sum(1 for char in text.lower() if char in 'aeiou')
 print(f" text has {vowels} vowels!")      
