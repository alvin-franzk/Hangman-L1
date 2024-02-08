import time
from os import system
import random
from random_word import RandomWords
r = RandomWords()

answer = []
blanks = []
guessedword = []
lettersused = []

def main():
    word = generateWord()
    lives = round(len(word) / 2)

    # Loop game
    guess = ''
    while lives != 0:
        printResult(word, checkGuess(guess))
        print("Lives:", lives)
        guess = input("Your guess: ")



def generateWord():
    with open('words_alpha.txt') as dict:
        words = dict.read().splitlines()
        word = random.choice(words)
        return word


def printResult(word, guess):
    if lives == round(len(word) / 2):
        print("Your word is:", end = " ")
        for letter in word:
            answer.append(letter)
        for x in range(len(word)):
            blanks.append(x)
            guessedword.append("_")
        


def checkGuess(guess):
    correctguess = 0
    lettercount = -1
    for letter in answer:
        lettercount += 1
        if guess == letter:
            blanks[lettercount] = answer[lettercount]
            guessedword[lettercount] = answer[lettercount]
            correctguess += 1
    if correctguess > 0:
        return True
    else:
        return False



main()