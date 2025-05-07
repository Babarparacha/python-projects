import random
words=['python','coding','games','computer','fun','learn']
while True:
    original_word=random.choice(words)
    #"game"=>['g','a','m','e']=>="agme"
    letters=list(original_word)
    random.shuffle(letters)
    scramble="".join(letters)
    print(f"scrambled word {scramble}")
    guess=input("what the word").lower()
    if guess==original_word:
     print("congrats you win!")
    else:
       print(f"sorry the correct word is {original_word} ") 
    again=input("you want to play again")
    if not again.startswith('y').lower():
       print("good bye")
       break   