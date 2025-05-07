import random
import time
import os

def clean_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == "nt" else "clear")

print("== Memory Sequence Game ==")
print("== Remember the sequence and type it back ==")
print("== Rules:")
print("== Watch a number appear one by one")
print("== After the sequence is shown, type it back in order")
print("== Each round adds one more number to remember")
print("== How far can you go? ==")

input("Press Enter to start...")
sequence = []
current_round = 1
game_over = False

while not game_over:
    sequence.append(random.randint(1, 5))

    clean_screen()
    print(f"Round {current_round}")
    print(f"Remember this sequence of {len(sequence)} numbers:")

    for number in sequence:
        time.sleep(0.7)
        print(number)
        time.sleep(0.7)
        clean_screen()

    print("Now repeat the sequence by typing each number, separated by spaces.")
    player_answer = input("> ")

    try:
        player_sequence = [int(num) for num in player_answer.split()]
    except ValueError:
        print("Please enter only numbers!")
        game_over = True
        continue

    if player_sequence == sequence:
        print(f"Congrats! You remembered all {len(sequence)} numbers!")
        current_round += 1
        time.sleep(2)
    else:
        print(f"Game over! You remembered {len(sequence) - 1} rounds correctly.")
        print("The correct sequence was:", " ".join(str(num) for num in sequence))
        game_over = True

    if game_over:
        play_again = input("Play again? yes/no: ").lower()
        if play_again.startswith('y'):
            sequence = []
            current_round = 1
            game_over = False
        else:
            print("Thanks for playing!")
