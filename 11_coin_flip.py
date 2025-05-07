import random
while True:
    guess=input('enter your guess (heads/tails):').lower()
    if guess!='heads' and guess!='tails':
     print("please enter heads/tails")
     continue
    flip=random.choice(['heads','tails'])
    print(f'coin show {flip}')
    if guess ==flip:
       print("you have won!")
    else:
       print("you have loss!")   
    agian=input("play again y/n:").lower()
    if not agian.startswith('y'):
       print('good bye!')
       break
          

