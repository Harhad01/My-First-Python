<<<<<<< HEAD
import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']
word_list = ["Lionel Messi", "Cristiano Ronaldo", "Pelé", "Maradona", "Johan Cruyff", 
             "Beckenbauer", "Zidane", "Costacurta", "Modric", "Platini", "Kroos",
             "Totti", "Puskás", "Thuram", "Garrincha", 
             "Van Basten", "Baresi", "Paolo Maldini", "Matthäus",  "Baggio", 
             "Romario", "Ronaldinho", "Thierry Henry", "Iniesta", "Xavi Hernández", "Pirlo",
             "Steven Gerrard", "Frank Rijkaard", "Gullit", "Rummenigge", "Gerd Müller"]

def choose_word():
    word = random.choice(word_list)
    return word.lower()


def display_game_state(hidden_word, guessed_letters, attempts_left):
    print(HANGMAN_PICS[len(HANGMAN_PICS) - attempts_left - 1])
    print("Word: " + " ".join(hidden_word))
    print("Guessed Letters: " + " ".join(guessed_letters))
    print(f"Attempts Left: {attempts_left}")
    
    
def get_player_guess(guessed_letters):
    #validate if its a single letter
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess)!=1:
            print("Only single letter allowed!")
        elif not guess.isalpha():
            print("Only letters are allowed!")
        elif guess in guessed_letters:
            print("You guessed it already! Try again.")
        else:
            return guess

def update_game_state(secret_word, hidden_word, guessed_letter):
    found = False 
    
    for i in range(len(secret_word)):
        if secret_word[i] == guessed_letter:
            hidden_word[i] = guessed_letter
            found = True 
    
    return found

def play_hangman():
    secret_word = choose_word()
    hidden_word = ["_"] * len(secret_word)
    guessed_letters = []
    attempts_left = 6
    game_over = False 
    
    while attempts_left > 0 and game_over == False:
        display_game_state(hidden_word, guessed_letters, attempts_left)
        
        guess = get_player_guess (guessed_letters)
        guessed_letters.append(guess)
        
        
        correct_guess = update_game_state(secret_word, hidden_word, guess)
        
        if not correct_guess:
            attempts_left -= 1
            print(f" Getting Cooked! The letter '{guess}' is not in the word.😔")
        
        if "_" not in hidden_word:
            display_game_state(hidden_word, guessed_letters, attempts_left)
            print("🎉Vamoss!!! You got the PRODIGY!!🎉")
            game_over = True
            break
            
    
    if attempts_left == 0 and not game_over:
        display_game_state(hidden_word, guessed_letters, attempts_left)
        print(f"Ran Extra time! The King was'{secret_word}'. Hope u beat next time!😛")

    play_again = input("Wanna go again? (yes/no): ").lower()
    if play_again == "yes":
        play_hangman()
    else:
        print("For the time being, See you later!⛳")
            
print("Welcome to Guessing THE PRODIGY'S of Game!!!⚽")
play_hangman()





=======
import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']
word_list = ["Lionel Messi", "Cristiano Ronaldo", "Pelé", "Maradona", "Johan Cruyff", 
             "Beckenbauer", "Zidane", "Costacurta", "Modric", "Platini", "Kroos",
             "Totti", "Ferenc Puskás", "Thuram", "Garrincha", 
             "Van Basten", "Baresi", "Paolo Maldini", "Matthäus",  "Baggio", 
             "Romario", "Ronaldinho", "Thierry Henry", "Iniesta", "Xavi Hernández", "Pirlo",
             "Steven Gerrard", "Frank Rijkaard", "Gullit", "Rummenigge", "Gerd Müller"]

def choose_word():
    word = random.choice(word_list)
    return word.lower()


def display_game_state(hidden_word, guessed_letters, attempts_left):
    print(HANGMAN_PICS[len(HANGMAN_PICS) - attempts_left - 1])
    print("Word: " + " ".join(hidden_word))
    print("Guessed Letters: " + " ".join(guessed_letters))
    print(f"Attempts Left: {attempts_left}")
    
    
def get_player_guess(guessed_letters):
    #validate if its a single letter
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess)!=1:
            print("Only single letter allowed!")
        elif not guess.isalpha():
            print("Only letters are allowed!")
        elif guess in guessed_letters:
            print("You guessed it already! Try again.")
        else:
            return guess

def update_game_state(secret_word, hidden_word, guessed_letter):
    found = False 
    
    for i in range(len(secret_word)):
        if secret_word[i] == guessed_letter:
            hidden_word[i] = guessed_letter
            found = True 
    
    return found

def play_hangman():
    secret_word = choose_word()
    hidden_word = ["_"] * len(secret_word)
    guessed_letters = []
    attempts_left = 6
    game_over = False 
    
    while attempts_left > 0 and game_over == False:
        display_game_state(hidden_word, guessed_letters, attempts_left)
        
        guess = get_player_guess (guessed_letters)
        guessed_letters.append(guess)
        
        
        correct_guess = update_game_state(secret_word, hidden_word, guess)
        
        if not correct_guess:
            attempts_left -= 1
            print(f" Getting Cooked! The letter '{guess}' is not in the word.😔")
        
        if "_" not in hidden_word:
            display_game_state(hidden_word, guessed_letters, attempts_left)
            print("🎉Vamoss!!! You got the PRODIGY!!🎉")
            game_over = True
            break
            
    
    if attempts_left == 0 and not game_over:
        display_game_state(hidden_word, guessed_letters, attempts_left)
        print(f"Ran Extra time! The King was'{secret_word}'. Hope u beat next time!😛")

    play_again = input("Wanna go again? (yes/no): ").lower()
    if play_again == "yes":
        play_hangman()
    else:
        print("For the time being, See you later!⛳")
            
print("Welcome to Guessing THE PRODIGY'S of Game!!!⚽")
play_hangman()




>>>>>>> 97e8131 (Save local work before sync)
