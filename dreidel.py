#Amaka Ukekwe
#Dreidel
#Start Work: 12/11/19
#Last Work: 12/1/19

import random

#check function
def check(currentPlayerTotals,currentPlayers,currentPotTotal,initialGroup,initialTotal,units):
  i = 0
  while i < len(currentPlayerTotals):
    #elimination (I forgot to end the game if a single player runs out of pieces but I left it since it's more realistic)
    if currentPlayerTotals[i] < 1:
      print(currentPlayers[i] + " has run out of " + units + ". They are out.")
      currentPlayers.remove(currentPlayers[i])
      currentPlayerTotals.remove(currentPlayerTotals[i])
      #game ends
      if len(currentPlayers) == 1:
        if currentPlayerTotals[0] == 0:
          print(currentPlayers[0] + " also ran out.\nNo one won :( Game Over!")
          break
        else:
          print(currentPlayers[0] + " has won!\nThey received " + str(initialGroup*initialTotal) + " " + units + ".\nGame Over")
          break
    else:
      i += 1
  if currentPotTotal <= 1:
    print("The pot has reached a total of " + str(currentPotTotal) + " " + units + ". Every player must add another one of their " + units + " to the pot.")
    for i in range(len(currentPlayerTotals)):
      currentPlayerTotals[i] -= 1
    currentPotTotal = initialTotal*initialGroup - sum(currentPlayerTotals)

#spin function
def spin(currentPlayerTotals,currentPlayers,currentPotTotal,initialGroup,initialTotal,units):
  for i in range(len(currentPlayers)):
    spinOptions = ["Nun", "Hey", "Shin", "Gimmel"]
    spinResult = random.choice(spinOptions)
    print("The dreidel has landed on " + spinResult + ".")

    #Nun function adds 0 pieces to player
    if spinResult == "Nun":
      print(currentPlayers[i] +  " has neither lost nor gained " + units + ".")
    #Hey function adds half of pot variable total
    elif spinResult == "Hey":
      if currentPotTotal % 2 != 0:
        currentPlayerTotals[i] += (currentPotTotal-1)/2
        currentPotTotal = initialTotal*initialGroup - sum(currentPlayerTotals)
      else:
        currentPlayerTotals[i] += currentPotTotal/2
        currentPotTotal = initialTotal*initialGroup - sum(currentPlayerTotals)
      print(currentPlayers[i] + " has received half the pot.")
    #Shin function subtracts piece from player
    elif spinResult == "Shin":
      currentPotTotal += 1
      currentPlayerTotals[i] -=1
      print(currentPlayers[i] +  " was forced to add one of their " + units + " to the pot.")
    #Gimmel function gives pot total to player
    elif spinResult == "Gimmel":
      currentPlayerTotals[i] += currentPotTotal
      currentPotTotal = 0
      print(currentPlayers[i] +  " received the whole pot!")

    if currentPotTotal <= 1:
      print("The pot has reached a total of " + str(currentPotTotal) + " " + units + ". Every player must add another one of their " + units + " to the pot.")
      for i in range(len(currentPlayerTotals)):
        currentPlayerTotals[i] -= 1
      currentPotTotal = initialTotal*initialGroup - sum(currentPlayerTotals)

    quit = input("(This player can quit by pressing 'q'.) ")
    if quit == "q":
      currentPlayerTotals[i] = 0

#greeting
print("Hello! Welcome to Dreidel Sim!")
print()

#number of players
playersQuantity = int(input("How many players would you like to include? "))
while playersQuantity <= 1:
  playersQuantity = int(input("How many players would you like to include?\n(Must be an integer greater than 1) "))
print()

#unit of currency
pieceType = input("Which type of piece would you like to play with? (ex. candy bars, dollars)\n(Please answer in the plural form) ")

#variables for number of pieces for each player
piecesAssign = int(input("How many " + pieceType + " each would you like to play with? "))
while piecesAssign < 2:
  piecesAssign = int(input("How many " + pieceType + " would you like to play with?\n(Must be an integer greater than 1) "))

print()

players = []
playerPieces = []

for i in range(playersQuantity):
  players.append("Player " + str(i+1))
  playerPieces.append(piecesAssign)

print("Each player has started with " + str(playerPieces[0]) + " " + pieceType + ".")

#variable for pieces in pot
potTotal = 0

#pieces added to pot in beginning
for i in range(len(playerPieces)):
  playerPieces[i] -= 1
  potTotal += 1

#intro
print("Each player has added one of their " + pieceType + " to the pot.\nThere are now " + str(potTotal) + " " + pieceType + " in the pot.")
print("Press any key to continue")
input()

#new round function
def newRound(currentPlayerTotals,currentPlayers,currentPotTotal,initialGroup,initialTotal,units):
  check(playerPieces,players,potTotal,playersQuantity,piecesAssign,pieceType)
  if len(currentPlayers) > 1:
    for i in range(len(currentPlayers)):
      print(currentPlayers[i] + ": " + str(currentPlayerTotals[i]) + " " + units)
    print("Each player will now spin the dreidel.")
    spin(playerPieces,players,potTotal,playersQuantity,piecesAssign,pieceType)
    check(playerPieces,players,potTotal,playersQuantity,piecesAssign,pieceType)
    if len(currentPlayers) > 1:
      print("The round has ended. Each player will now add one of their " + units + " to the pot.")
      for i in range(len(currentPlayerTotals)):
        currentPlayerTotals[i] -= 1
      currentPotTotal = initialTotal*initialGroup - sum(currentPlayerTotals)
      print("Current Pot Total: " + str(currentPotTotal) + " " + units)
      print("Press any key to start the next round.")
      input()

while len(players) > 1:
  newRound(playerPieces,players,potTotal,playersQuantity,piecesAssign,pieceType)
