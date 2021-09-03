"""
name: dreidel.py
author: Uzo Ukekwe
version: python 3.8
purpose: simulates the traditional Jewish game dreidel
"""

import random


def new_round(players, player_pieces, piece_type, pcs_in_pot):
    """
    Runs through the current round
    :param players: the list of players in the game
    :param player_pieces: the list of piece quantities for each player
    :param piece_type: the unit of currency the players will use
    :param pcs_in_pot: the total number of pieces in the pot
    """
    # body


def new_game(num_players, piece_type, pcs_per_player):
    """
    Initiates a series of rounds using the new game parameters
    :param num_players: the number of players at the start of the game
    :param piece_type: the unit of currency the players will use
    :param pcs_per_player: the number of pieces each player starts with
    """
    players = []
    player_pieces = []     # matches indices to keep track of pieces each player has

    # set player names and initial piece totals
    for i in range(num_players):
        players.append("Player " + str(i + 1))
        player_pieces.append(pcs_per_player)
    print("Each player has started with " + str(pcs_per_player) + " " + piece_type + ".")

    # create pot and add pieces to start
    pcs_in_pot = 0
    for i in range(len(player_pieces)):
        player_pieces[i] -= 1
        pcs_in_pot += 1
    print("Each player has added one of their " + piece_type + " to the pot.\n"
          "There are now " + str(pcs_in_pot) + " " + piece_type + " in the pot.")

    print("Press any key to continue")
    input()

    new_round(players, player_pieces, piece_type, pcs_in_pot)


'''
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


# new round function
def newRound(current_player_totals, current_players, current_pot_total, initial_group, initial_total, units):
    check(playerPieces, players, pcs_in_pot, playersQuantity, piecesAssign, pieceType)
    if len(current_players) > 1:
        for i in range(len(current_players)):
            print(current_players[i] + ": " + str(current_player_totals[i]) + " " + units)
        print("Each player will now spin the dreidel.")
        spin(playerPieces, players, pcs_in_pot, playersQuantity, piecesAssign, pieceType)
        check(playerPieces, players, pcs_in_pot, playersQuantity, piecesAssign, pieceType)
        if len(current_players) > 1:
            print("The round has ended. Each player will now add one of their " + units + " to the pot.")
            for i in range(len(current_player_totals)):
                current_player_totals[i] -= 1
            current_pot_total = initial_total * initial_group - sum(current_player_totals)
            print("Current Pot Total: " + str(current_pot_total) + " " + units)
            print("Press any key to start the next round.")
            input()


while len(players) > 1:
    newRound(playerPieces, players, pcs_in_pot, playersQuantity, piecesAssign, pieceType)
'''


def main():
    """
    Sets up the players and pieces, running each round until someone wins.
    """
    print("Hello! Welcome to Dreidel Sim!\n")

    # set the number of players
    num_players = int(input("How many players would you like to include? \n"))
    while num_players <= 1:
        num_players = int(input(
            "How many players would you like to include?\n"
            "(Must be an integer greater than 1) \n"))

    # set the unit of currency
    piece_type = input("Which type of piece would you like to play with?"
                       "(ex. candy bars, dollars)\n"
                       "(Please answer in the plural form) \n")

    # set the number of pieces each player starts with
    pcs_per_player = int(input("How many " + piece_type +
                               " each would you like to play with? \n"))
    while pcs_per_player < 2:
        pcs_per_player = int(
            input("How many " + piece_type + " would you like to play with?"
                                             "\n(Must be an integer greater than 1) \n"))

    new_game(num_players, piece_type, pcs_per_player)


if __name__ == "__main__":
    main()
