import random
playing=True
while playing:
    secret_number=random.randint(1,10)
    # secret_number=random.randint(1,100)
    attempts=0
    max_attempt=10
    game_over=False
    while attempts<max_attempt and not game_over:
        try:
            guess=int(input(f"attempt {attempts+1}/{max_attempt}. enter your guess:"))
        except ValueError:
            print("please enter a valid number")
            continue
        attempts+=1
        if guess<secret_number:
            print("too low. pleade try a higher number")
        elif guess>secret_number:
            print("too high")       
        else:
            print(f'congrats! you guess the number {secret_number} in {attempts}')
            game_over=True 
        if attempts<max_attempt and not game_over:
            print(f'you have {max_attempt-attempts} attempt left ')  
    if not game_over:
        print(f" game over the number was {secret_number}")
    play_again=input("would you like to play agian y/n:").lower()              
    if  play_again.startswith('y').lower():
       print("new game  starting....")
    else:
        print("game over")   
        break   