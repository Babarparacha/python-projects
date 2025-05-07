import random
print("music recommender")

genres={
    'rock':['ac/dc','queen','led','zeppelin'],
    'pop':['taylor swift','jack','hampsjire','lady gaga'],
    'hit-pop':['jistin bieber','queen','led','dg'],
}
choice=input('what genre do you like?(rock/pop/hit-pop):')
if choice not in genres:
    print("sorry, i do not know that music")
else:
    print(f"check out {random.choice(genres[choice])}")