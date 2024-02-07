import time
from os import system
from random_word import RandomWords
r = RandomWords()

intro = "WELCOME TO HANGMAN!"

def startup():
    for x in range(10):
        print("*", end = " ")
        time.sleep(0.1)
    time.sleep(0.1)
    print('\n')
    for letter in intro:
        print(letter, end = "")
        time.sleep(0.1)
    print('\n')
    time.sleep(0.1)
    for x in range(10):
        print("*", end = " ")
        time.sleep(0.1)
    print('\n')
    
    input("Press Enter to continue...")
    system('cls')
def hangman(word):    
    print("Your word is:", end = " ")
    for letter in word:
        answer.append(letter)
    for x in range(len(word)):
        blanks.append(x)
        guessedword.append("_")
    #print(word)
def checkguess(guess):
    correctguess = 0
    lettercount = -1
    for x in answer:
        lettercount += 1
        if guess == x:
            blanks[lettercount] = answer[lettercount]
            guessedword[lettercount] = answer[lettercount]
            correctguess += 1
    if correctguess > 0:
        return True
    else:
        return False
def updateblanks():
    count = -1
    for x in blanks:
        if isinstance(x, int):
            count += 1
            guessedword[count] = "_"  
        else:
            count += 1
def getword():
    word = r.get_random_word()
    return word
def guiword():
    for x in range(len(word)):
        print(guessedword[x], end = " ")
    print('\n')
    print("No. of tries left: ", tries)
    print('\n')

game = 1   
while(game == 1):
    answer = []
    blanks = []
    guessedword = []
    word = getword()
    hangman(word)
    tries = int((len(word) / 2) + 1)
    lettersused = []
    completedword = 0
    while(tries != 0):
        guiword()
        guess = input("Input guess: ")
        if checkguess(guess) == True and guess not in lettersused:
            print(guess, " is correct.")
            lettersused.append(guess)
            completedword += 1
            if completedword == len(word):
                print("Congratulations! You guessed the word!")
                break
        elif checkguess(guess) == True and guess in lettersused:
            print(guess, " has already been guessed.")
        elif checkguess(guess) == False and tries == 1:
            print(guess, " is incorrect.",'\n\n', "You ran out of tries.", '\n\n', "The word was: ", word)
            print('\n')
            break
        else:
            print(guess, " is incorrect. Try again.")
            tries -= 1
        updateblanks()
    coin = input("Try again? Y/N: ")
    if coin == 'y' or 'Y':
        continue
    elif coin == 'n' or 'N':
        game = 0
        break
print("Thanks for playing!")
