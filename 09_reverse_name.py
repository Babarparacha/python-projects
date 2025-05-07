
while True:
 name=input("enter your name to reverse it:")
 if not name:
  break
 reversr_name=name[::-1]
 print(f"your reverse name is {reversr_name}")
 print(f"in a parellel uviverse, they call you  {reversr_name.title()}")
 answer=input("try antoher one? y/n")
 if answer!='y':
  break