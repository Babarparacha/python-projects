import time
while True:
   try: 
     seconds=int(input("enter second to countdown from:"))
     if seconds<=0:
        print("please enter valid seconds")
        continue
       
     print(f"start countdown from {seconds} seconds:")
     for i in range(seconds,0,-1):
        print(f"{i} seconds left...")
        time.sleep(1)
     print("count down complete")
     again= input("start again y/n:").lower()
     if not again.startswith('y'):
        print("good bye")
        break 
   except ValueError:
    print("please enter a number")     