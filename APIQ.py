import random
import importlib
import API.E

importlib.reload(API.E)
secret_word = API.E.choosenName


HANGMAN_STAGES = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========='''
]



def display_hangman(wrong_guesses):
    print(HANGMAN_STAGES[wrong_guesses])


def display_word(secret_word, guessed_letters):
    displayed = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    print(displayed)
    return displayed


def play_hangman():
    importlib.reload(API.E)
    secret_word = API.E.choosenName
    print(f"secret word :{secret word}")
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = len(HANGMAN_STAGES) - 1

    print("Game started!")

    while wrong_guesses < max_wrong_guesses:
        display_hangman(wrong_guesses)
        current_state = display_word(secret_word, guessed_letters)

        if "_" not in current_state:
            print(f" You guessed the word: {secret_word}")
            return

        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Incorrect guess!")

    # If loop ends
    display_hangman(wrong_guesses)
    print(f" You ran out of guesses! The word was: {secret_word}")


if __name__ == "__main__":
    play_hangman()
