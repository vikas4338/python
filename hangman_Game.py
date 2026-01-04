import random
print("welcome to the Game, Hangman!!")

print('''                                           
88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  8b,dPPYba, 
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  88P'   `"8a
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  88       88  
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  88       88  
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  88       88  
                                    aa,    ,88                                
                                     "Y8bbdP"                               
''')

word_list = [
    "dog", "cat", "cow", "pig"
]

animal_words = [
    "dog", "cat", "horse", "cow", "pig", "lion", "tiger", "elephant", "rabbit", "bear",
    "fox", "wolf", "deer", "goat", "sheep", "duck", "fish", "frog", "turtle", "snake",
    "bird", "owl", "parrot", "squirrel", "monkey", "giraffe", "zebra", "kangaroo",
    "dolphin", "whale", "camel", "wolf", "rat", "mouse", "bee", "butterfly", "shark",
    "otter", "raccoon", "leopard", "horse", "donkey", "chicken", "goose", "eagle",
    "penguin", "hedgehog", "bear", "panda", "gorilla", "zebra", "seal", "owl"
]

hangman_stages = [
    # 0 wrong guesses
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    # 1 wrong guess
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    # 2 wrong guesses
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    # 3 wrong guesses
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    # 4 wrong guesses
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    # 5 wrong guesses
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    # 6 wrong guesses — full hangman
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

chosen_word = random.choice(word_list)
# print(chosen_word)
wrong_guesses = 0
display = ["_"] * len(chosen_word)
print(display)

while True:
    # pick a random unrevealed letter
    unrevealed = [c for i, c in enumerate(chosen_word) if display[i] == "_"]
    if not unrevealed:
        print("No more hints — all letters revealed!")
        break

    hint_needed = input("Do you need hint? type yes/y or no/n? ")
    if hint_needed not in "yes, y":
        break

    hint_letter = random.choice(unrevealed)

    print(hint_letter)
    indexes = [i for i, c in enumerate(chosen_word) if c == hint_letter]
    for index, letter in enumerate(display):
        if index in indexes:
            display[index] = hint_letter
            print(display)

while wrong_guesses < 6 and "_" in display:
    guess = (input("Type a letter to guess the word ")).lower()
    # print(guess in chosen_word)
    if guess in chosen_word and guess not in display:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter
    else:
        wrong_guesses += 1
        print(hangman_stages[wrong_guesses])
    print(display)

if "_" not in display:
    display_string = "".join(display)
    print(f"You Won!! Word \"{display_string}\" guessed successfully")
else:
    print("You loose!!")
