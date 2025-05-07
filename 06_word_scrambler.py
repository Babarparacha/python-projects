print("word scrambler")
import random
while True:
    word=input("enter a word to scrambler (or quit):")
    if word.lower()=='quit':
        print("good bye")
        break
    # everyone=['e','v','e','','r','y','o','n','e']
    letters=list(word)
    random.shuffle(letters)
    print(f"scrambled:{"".join(letters)}")