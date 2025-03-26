"""
gameboyUnadvanced.py
Brycen Siv

Create a basic game selector and player. 
The selection screen should display this:
Select a game!
1. Roulette
2. Math Quiz
3. The Waiting Game
4. Quit

After this it should take an input for the number corresponding to the game. Be sure to error check that the number is indeed between 1 and 4.
If not, please output Invalid selection. Please pick a valid game number. and ask again.
The Selections should use functions to run the particular game. If you code the entire game within the if condition, it'll be points off.

roulette:
At the beginning seed the random number generator with the seed 10 with random.seed(10) This is for grading purposes.
Afterwards, generate a random number between 1 and 10. Prompt the player to guess by asking 
Guess a number between 1 and 10: 
If the guess right, print You Win! Otherwise print Wrong! Guess again! before prompting them for another input with the same message as above.
mathQuiz:
As before, seed the random number generator with the seed 10. Now generate 2 random numbers and ask the user
What is {firstNumber} + {secondNumber}? 
If they guess right, once again print You Win! and if they guess wrong print Wrong! Guess again! before repeating the same prompt as above. 
theWaitingGame:
Wait 5 seconds, then print You Win! then return.
Upon completion of any game, the game selection should repeat to prompt the user to select another game. This should only end if the user inputs 4 as their game selection in order to quit.
"""
import random
import time

# Roulette
def Roulette():
    random.seed(10)
    rnum = random.randint(1,10)
    roulette = int(input("Guess a number between 1 and 10: "))
    while True:
        if roulette == rnum:
            print("You Win!")
            choosegame()
            break
        else:
            print("Wrong! Guess again!")
        roulette = int (input("Guess a number between 1 and 10: "))
# Math Quiz
def mathquiz():
    random.seed(10)
    mathnum = random.randint(1,10)
    mathnum2 = random.randint(1,10)
    asknum = int(input(f"What is {mathnum} + {mathnum2}? "))
    while True:
        if asknum == mathnum + mathnum2:
            print("You Win!")
            choosegame()
            break
        else:
            print("Wrong! Guess again!")
        asknum = int(input(f"What is {mathnum} + {mathnum2}? "))
# The Waiting Game
def waitinggame():
    time.sleep(5)
    print("You Win!")
    choosegame()
# Game Selection
def choosegame():
    print("Select a game!\n 1. Roulette\n 2. Math Quiz\n 3. The Waiting Game\n 4. Quit")
    num = int (input(""))
    if num == 1:
        Roulette()
    if num == 2:
        mathquiz()
    if num == 3:
        waitinggame()
    if num == 4:
        return
# If the user input any number greater than 3 or less than 1, it would give an invalid message and ask again.
    while (num < 1 or num > 3):
        print("Invalid selection. Please pick a valid game number.")
        print("Select a game!\n 1. Roulette\n 2. Math Quiz\n 3. The Waiting Game\n 4. Quit")
        num = int (input())

choosegame()
