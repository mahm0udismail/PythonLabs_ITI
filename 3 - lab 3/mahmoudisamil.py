import random

l=["Abdallah","hangman","word","maximum","show","wrong","complete","occurences","previous","guess"]
random_index = random.randint(0, len(l) - 1)
name = str(input("please enter your name: "))

word=l[random_index]
hidden_word = ["_"] * len(word)
print(word,' '.join(hidden_word),name)


for i in range(7):
    guess=input("guess a letter: ")
    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                hidden_word[index] = guess
        print(f"Correct! Current word: {' '.join(hidden_word)}")
    else:
        print(f"Sorry, the letter '{guess}' is not in the word. Current word: {' '.join(hidden_word)}")
    if guess == word:
        print("the word is correct! congratulations")
        break
    print(i)