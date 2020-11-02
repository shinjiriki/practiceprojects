# Rock, Paper, Scissors Game
# Make a rock-paper-scissors game where it is the player vs the computer.
# The computer’s answer will be randomly generated, while the program will ask the user for their input.

import random

choices = ['Paper', 'Scissor', 'Rock']
rounds = 1
computerscore = 0
userscore = 0

print("Welcome to Rock, Paper, Scissor Game. There will be 10 Rounds. ")

while rounds < 11:
    win = False
    computer = random.choice(choices).lower()
    user = input("Choose Rock, Paper or Scissor : Round {} \n".format(rounds)).lower()
    rounds += 1
    if user == computer:
        print("It's a tie")
        computerscore -= 1
    if user == 'rock':
        if computer == 'paper':
            print("You lose")
        if computer == 'scissor':
            print("You win")
            win = True
    if user == 'paper':
        if computer == 'scissor':
            print("You lose")
        if computer == 'rock':
            print("You win")
            win = True
    if user == 'scissor':
        if computer == 'rock':
            print("You lose")
        if computer == 'paper':
            print("You win")
            win = True
    if win:
        userscore += 1
    else:
        computerscore += 1

print("User : ", userscore)
print("Computer : ", computerscore)
tie = 10 - userscore - computerscore
print("Tie : ", tie)

if userscore > computerscore:
    print("You win the game!, Congratulations")
elif userscore == computerscore:
    print("It's a tie")
else:
    print("You lose, goodluck next time")
