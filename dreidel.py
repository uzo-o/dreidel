"""
name: dreidel.py
author: Uzo Ukekwe
version: python 3.8
purpose: simulates the traditional Jewish game dreidel
"""

import random


# check function
def check(current_player_totals, current_players, current_pot_total, initial_group, initial_total, units):
    i = 0
    while i < len(current_player_totals):
        # elimination
        if current_player_totals[i] < 1:
            print(current_players[i] + " has run out of " + units + ". They are out.")
            current_players.remove(current_players[i])
            current_player_totals.remove(current_player_totals[i])
            # game ends
            if len(current_players) == 1:
                if current_player_totals[0] == 0:
                    print(current_players[0] + " also ran out.\nNo one won :( Game Over!")
                    break
                else:
                    print(current_players[0] + " has won!\nThey received " + str(
                        initial_group * initial_total) + " " + units + ".\nGame Over")
                    break
        else:
            i += 1
    if current_pot_total <= 1:
        print("The pot has reached a total of " + str(
            current_pot_total) + " " + units + ". Every player must add another one of their " + units + " to the pot.")
        for i in range(len(current_player_totals)):
            current_player_totals[i] -= 1
        current_pot_total = initial_total * initial_group - sum(current_player_totals)


# spin function
def spin(current_player_totals, current_players, current_pot_total, initial_group, initial_total, units):
    for i in range(len(current_players)):
        spin_options = ["Nun", "Hey", "Shin", "Gimel"]
        spin_result = random.choice(spin_options)
        print("The dreidel has landed on " + spin_result + ".")

        # Nun function adds 0 pieces to player
        if spin_result == "Nun":
            print(current_players[i] + " has neither lost nor gained " + units + ".")
        # Hey function adds half of pot variable total
        elif spin_result == "Hey":
            if current_pot_total % 2 != 0:
                current_player_totals[i] += (current_pot_total - 1) / 2
                current_pot_total = initial_total * initial_group - sum(current_player_totals)
            else:
                current_player_totals[i] += current_pot_total / 2
                current_pot_total = initial_total * initial_group - sum(current_player_totals)
            print(current_players[i] + " has received half the pot.")
        # Shin function subtracts piece from player
        elif spin_result == "Shin":
            current_pot_total += 1
            current_player_totals[i] -= 1
            print(current_players[i] + " was forced to add one of their " + units + " to the pot.")
        # Gimel function gives pot total to player
        elif spin_result == "Gimel":
            current_player_totals[i] += current_pot_total
            current_pot_total = 0
            print(current_players[i] + " received the whole pot!")

        if current_pot_total <= 1:
            print("The pot has reached a total of " + str(current_pot_total) + " " + units +
                  ".\n Every player must add another one of their " + units + " to the pot.")
            for i in range(len(current_player_totals)):
                current_player_totals[i] -= 1
            current_pot_total = initial_total * initial_group - sum(current_player_totals)

        quit = input("(This player can quit by pressing 'q'.) ")
        if quit == "q":
            current_player_totals[i] = 0


# greeting
print("Hello! Welcome to Dreidel Sim!")
print()

# number of players
playersQuantity = int(input("How many players would you like to include? "))
while playersQuantity <= 1:
    playersQuantity = int(input("How many players would you like to include?\n(Must be an integer greater than 1) "))
print()

# unit of currency
pieceType = input(
    "Which type of piece would you like to play with? (ex. candy bars, dollars)\n(Please answer in the plural form) ")

# variables for number of pieces for each player
piecesAssign = int(input("How many " + pieceType + " each would you like to play with? "))
while piecesAssign < 2:
    piecesAssign = int(
        input("How many " + pieceType + " would you like to play with?\n(Must be an integer greater than 1) "))

print()

players = []
playerPieces = []

for i in range(playersQuantity):
    players.append("Player " + str(i + 1))
    playerPieces.append(piecesAssign)

print("Each player has started with " + str(playerPieces[0]) + " " + pieceType + ".")

# variable for pieces in pot
potTotal = 0

# pieces added to pot in beginning
for i in range(len(playerPieces)):
    playerPieces[i] -= 1
    potTotal += 1

# intro
print("Each player has added one of their " + pieceType + " to the pot.\nThere are now " + str(
    potTotal) + " " + pieceType + " in the pot.")
print("Press any key to continue")
input()


# new round function
def newRound(current_player_totals, current_players, current_pot_total, initial_group, initial_total, units):
    check(playerPieces, players, potTotal, playersQuantity, piecesAssign, pieceType)
    if len(current_players) > 1:
        for i in range(len(current_players)):
            print(current_players[i] + ": " + str(current_player_totals[i]) + " " + units)
        print("Each player will now spin the dreidel.")
        spin(playerPieces, players, potTotal, playersQuantity, piecesAssign, pieceType)
        check(playerPieces, players, potTotal, playersQuantity, piecesAssign, pieceType)
        if len(current_players) > 1:
            print("The round has ended. Each player will now add one of their " + units + " to the pot.")
            for i in range(len(current_player_totals)):
                current_player_totals[i] -= 1
            current_pot_total = initial_total * initial_group - sum(current_player_totals)
            print("Current Pot Total: " + str(current_pot_total) + " " + units)
            print("Press any key to start the next round.")
            input()


while len(players) > 1:
    newRound(playerPieces, players, potTotal, playersQuantity, piecesAssign, pieceType)
