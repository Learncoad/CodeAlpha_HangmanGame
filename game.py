import random 

#Predifin words
wordList = ['python','flask','developer','hangman','precess','program','django']

chosen_word = random.choice(wordList)

guessedletter = []
incorrect_guess = 0
maxAttempts = 6

def display():
    display = ""
    for letter in chosen_word:
        if letter in guessedletter:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

name = input("Enter you name: ")
print(f"Hey, {name} welcome to Hangman Game!")
print(display()) 

while incorrect_guess < maxAttempts:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single valid letter!")
        continue

    if guess in guessedletter:
        print("You already guessed that letters!")
        continue

    guessedletter.append(guess)

    if guess in chosen_word:
        print("Correct guess!")
    else:
        incorrect_guess += 1
        print(f"Wrong! attempts left: {maxAttempts-incorrect_guess}")

    current_display = display()
    print("\nWord:",current_display)

    if "_" not in current_display:
        print("\nCongratulations, You Won! The word was: ",chosen_word)
        break

if incorrect_guess == maxAttempts:
    print("\nYou Lost! The word was: ",chosen_word)