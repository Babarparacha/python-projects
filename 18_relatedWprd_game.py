import random
import time

word_pairs = {
    "sky": ['blue', 'cloud', 'bird', 'fly', 'sun'],
    "water": ['drink', 'ocean', 'fish', 'swim', 'boat'],
    "food": ['eat', 'cook', 'tasty', 'meal', 'restaurant'],
    "music": ['song', 'dance', 'listen', 'band', 'rhythm'],
    "book": ['read', 'story', 'page', 'author', 'library'],
    "tree": ['leaf', 'green', 'forest', 'wood', 'shade'],
    "car": ['drive', 'road', 'wheel', 'travel', 'speed'],
    "dog": ['pet', 'bark', 'walk', 'loyal', 'puppy'],
}

score = 0
rounds = 0

while True:
    prompt = random.choice(list(word_pairs.keys()))
    related_words = word_pairs[prompt]  # Fixed this line to use square brackets for access

    print(f"Prompt word: {prompt.lower()}")
    print("Quick! Type a word related to this prompt")

    start_time = time.time()
    response = input("> ").lower().strip()
    response_time = time.time() - start_time

    print(f"Response time: {response_time:.2f} seconds")  # Show response time with 2 decimals

    # Check if the response is related
    if response in related_words:
        points = max(1, 5 - int(response_time))  # Deduct points based on response time
        score += points  # Accumulate score
        print(f"Good association! +{points} points (Answered in {response_time:.2f}s)")
    else:
        print(f"Not a common association. Related words include: {', '.join(related_words)}")

    rounds += 1
    print(f"Score: {score}/{rounds * 5} possible points")

