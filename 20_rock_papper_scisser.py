import random
import time

def display_welcome():
    print('Rules:')
    print("Rock crushes Scissors")
    print("Scissors cut Paper")
    print("Paper covers Rock")
    print("First to win 3 rounds is the champion!")

def get_user_choice():
    while True:
        print("\nMake Your Choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")

def get_computer_choice():
    return random.randint(1, 3)

def convert_choice_to_text(choice):
    options = {1: "Rock", 2: "Paper", 3: "Scissors"}
    return options[choice]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif ((user_choice == 1 and computer_choice == 3) or
          (user_choice == 3 and computer_choice == 2) or
          (user_choice == 2 and computer_choice == 1)):
        return "user win"
    else:
        return "computer win"

def display_round_result(user_choice, computer_choice, result):
    user_text = convert_choice_to_text(user_choice)
    computer_text = convert_choice_to_text(computer_choice)
    print(f"\nYou chose: {user_text}")
    print("Computer choosing...")
    time.sleep(1)
    print(f"Computer chose: {computer_text}")
    if result == 'tie':
        print("It's a tie!")
    elif result == "user win":
        print("You win the round!")
    else:
        print("Computer wins the round!")

def play_game():
    """Main game function"""
    while True:
        display_welcome()
        user_score = 0
        computer_score = 0
        target_score = 3
        round_num = 1

        while user_score < target_score and computer_score < target_score:
            print(f"\nRound {round_num} ===")
            print(f"Score: You {user_score} - {computer_score} Computer")
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            result = determine_winner(user_choice, computer_choice)
            display_round_result(user_choice, computer_choice, result)

            if result == "user win":
                user_score += 1
            elif result == "computer win":
                computer_score += 1

            round_num += 1

        print("\nGame Over")
        print(f"Final Score: You {user_score} - {computer_score} Computer")
        if user_score > computer_score:
            print("Congrats! You win the game!")
        else:
            print("Computer wins the game.")

        play_again = input("\nPlay again? (yes/no): ").lower()
        if not play_again.startswith('y'):
            print("Thanks for playing!")
            break

# Start the game
play_game()
