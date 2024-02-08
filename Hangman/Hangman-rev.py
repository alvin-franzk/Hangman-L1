import time
from os import system
import random
from random_word import RandomWords
r = RandomWords()

# variables
answer = []
guessedword = []
lettersused = []

def main():
    word = generateWord()
    global tries
    tries = round(len(word) / 2) + 1

    # Loop game
    while tries != 0:
        hangman(word)
        print("\nTries:", tries)
        guess = input("Your guess: ")        
        checkGuess(guess)


def generateWord():
    with open('words_alpha.txt') as dict:
        words = dict.read().splitlines()
        word = random.choice(words)

    # storing word to array answer
    for letter in word:
        answer.append(letter)

    # storing array blanks/underscores
    for x in range(len(word)):
        guessedword.append("_")

    return word


def hangman(word):
    system('cls')
    print("Your word is:", end = " ")

    for x in range(len(word)):
        print(guessedword[x], end = " ")
        

def checkGuess(guess):
    incorrect = 0
    if guess not in lettersused:
        # update letters used
        lettersused.append(guess)

        # check letter/guess
        for letter in answer:
            if letter == guess:
                # correct guess
                guessedword[answer.index(letter)] = letter
            else:
                incorrect += 1

        if incorrect != 0:
            # incorrect guess
            global tries
            tries -= 1
            return 1
        else:
            # correct guess / OK status
            return 0
    else:
        # same guess
        return 2
    

main()