import random
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

    def_current_word(word,guessed_letters):
    displayed = ""
    for letter in word :
        if letter in guessed_letters :
            display += letter+ " "
      else:
        display += "_"
        print (display)

def play_hangman():
#  secret_word
guessed_letters =[]
wrong_guesses = 0
max_wrong_guesses = len(HANGMANSTAGES) - 1

print ( "game started")

while wrong_guesses < max_wrong_guesses and "_" in display_game_state(secret_word,guessed_letters):
    display_hangman(wrong_guesses)
    display_game_state (secret_words , guessed_letters)
    print(f"Guessed letters : {','. join (sorted (guessed letters))}") 

    guess = input("guess a letter : ").lower()

    if not guess.isalpha() or len(guess) ! = 1:
      print("Please enter a single letter .")
    continue
   if guess in guessed_letters:
      print(" You already guessed that letter")
    continue



