"""
name: dreidel.py
author: Uzo Ukekwe
version: python 3.8
purpose: simulates the traditional Jewish game dreidel
"""

import random


def nun(current_player, piece_type):
    """
    Add/remove 0 pieces from player when dreidel lands on Nun
    :param current_player: the player who spun the dreidel
    :param piece_type: the unit of currency the players are using
    """
    print(current_player + " has neither lost nor gained " + piece_type + ".")


def hey(current_player, current_player_total, pcs_in_pot):
    """
    Add half of pot total to player total when dreidel lands on Hey
    :param current_player: the player who spun the dreidel
    :param current_player_total: num of pieces belonging to the current player
    :param pcs_in_pot: the total number of pieces in the pot
    :return the new current player total and pot total
    """
    if pcs_in_pot % 2 == 0:
        winnings = pcs_in_pot / 2
    else:
        winnings = (pcs_in_pot - 1) / 2

    pcs_in_pot -= winnings
    current_player_total += winnings

    print(current_player + " has received half the pot.")

    return current_player_total, pcs_in_pot


def shin(current_player, current_player_total, piece_type, pcs_in_pot):
    """
    Remove one piece from player when dreidel lands on Shin
    :param current_player: the player who spun the dreidel
    :param current_player_total: num of pieces belonging to the current player
    :param piece_type: the unit of currency the players are using
    :param pcs_in_pot: the total number of pieces in the pot
    :return the new current player total and pot total
    """
    pcs_in_pot += 1
    current_player_total -= 1

    print(current_player + " was forced to add one of their " + piece_type +
          " to the pot.")

    return current_player_total, pcs_in_pot


def gimel(current_player, current_player_total, pcs_in_pot):
    """
    Give entire pot to player when dreidel lands on Gimel
    :param current_player: the player who spun the dreidel
    :param current_player_total: num of pieces belonging to the current player
    :param pcs_in_pot: the total number of pieces in the pot
    :return the new current player total and pot total
    """
    current_player_total += pcs_in_pot
    pcs_in_pot -= pcs_in_pot

    print(current_player + " received the whole pot!")

    return current_player_total, pcs_in_pot


def eliminate_player(current_player, current_player_total, players,
                     player_pieces, piece_type, pcs_in_pot, total_piece_count):
    """
    Eliminate player if they have run out of pieces
    :param current_player: the player who spun the dreidel
    :param current_player_total: num of pieces belonging to the current player
    :param players: the list of players in the game
    :param player_pieces: the list of piece quantities for each player
    :param piece_type: the unit of currency the players are using
    :param pcs_in_pot: the total number of pieces in the pot
    :param total_piece_count: the number of pieces that must always be present
    :return new pot total, whether or not player was eliminated
    """
    eliminated = False
    if current_player_total == 0:
        print(current_player + " has run out of " + piece_type +
              ". They are out.")
        players.remove(current_player)
        player_pieces.remove(current_player_total)
        pcs_in_pot = total_piece_count - sum(player_pieces)
        eliminated = True

        # end game if one player remains
        if len(players) == 1:
            if player_pieces[0] == 0:
                print(players[0] + " also ran out.\nNo one won :(")
            else:
                print(players[0] + " has won!\nThey get all " +
                      str(total_piece_count) + " " + piece_type + ".")
            print("GAME OVER")

    return pcs_in_pot, eliminated


def check(players, player_pieces, piece_type, pcs_in_pot, total_piece_count,
          current_player_index):
    """
    Check if any player or the pot has run out of pieces and rectify this
    :param players: the list players in the game
    :param player_pieces: the list of piece quantities for each player
    :param piece_type: the unit of currency the players are using
    :param pcs_in_pot: the total number of pieces in the pot
    :param total_piece_count: the number of pieces that must always be present
    :param current_player_index: index of player who spun the dreidel last
    :return new pot total, lower index eliminations
    """
    lower_index_elims = 0  # num of players whose turn comes before the next player that have been eliminated

    i = 0
    while i < len(players):
        if player_pieces[i] == 0:
            pcs_in_pot, dummy = eliminate_player(players[i], player_pieces[i],
                                                 players, player_pieces, piece_type,
                                                 pcs_in_pot, total_piece_count)
            if i <= current_player_index:
                lower_index_elims += 1
            if len(players) == 1:
                break
        # doesn't increment list if someone was eliminated to avoid skipping players
        else:
            i += 1

    # restock empty pot
    if pcs_in_pot == 0:
        print("The pot is empty.\n"
              "Every player must add another one of their "
              + piece_type + " to it.")
        i = 0
        while i < len(players):
            player_pieces[i] -= 1
            pcs_in_pot += 1
            old_num_players = len(players)
            pcs_in_pot, eliminated = eliminate_player(players[i], player_pieces[i],
                                                      players, player_pieces, piece_type,
                                                      pcs_in_pot, total_piece_count)
            if eliminated and i <= current_player_index:
                lower_index_elims += 1

            # if someone before the end of the list was eliminated, don't increment
            if eliminated and i != old_num_players-1:
                i = i
            else:
                i += 1

    return pcs_in_pot, lower_index_elims


def spin(current_player, current_player_total, piece_type, pcs_in_pot):
    """
    Give each player the chance to spin the dreidel
    :param current_player: the player who is spinning the dreidel
    :param current_player_total: num of pieces belonging to the current player
    :param piece_type: the unit of currency the players are using
    :param pcs_in_pot: the total number of pieces in the pot
    :return the new current player total and pot total
    """
    spin_options = ["Nun", "Hey", "Shin", "Gimel"]
    spin_result = random.choice(spin_options)
    print("\nThe dreidel has landed on " + spin_result + ".")

    if spin_result == "Nun":
        nun(current_player, piece_type)
    elif spin_result == "Hey":
        current_player_total, pcs_in_pot = hey(current_player,
                                               current_player_total, pcs_in_pot)
    elif spin_result == "Shin":
        current_player_total, pcs_in_pot = shin(current_player, current_player_total,
                                                piece_type, pcs_in_pot)
    elif spin_result == "Gimel":
        current_player_total, pcs_in_pot = gimel(current_player,
                                                 current_player_total, pcs_in_pot)

    forfeit = input("(This player can forfeit by pressing 'f'.) ")
    if forfeit == "f":
        pcs_in_pot += current_player_total
        current_player_total -= current_player_total

    return current_player_total, pcs_in_pot


def play_rounds(players, player_pieces, piece_type, pcs_in_pot, total_piece_count):
    """
    Run through each round
    :param players: the list of players in the game
    :param player_pieces: the list of piece quantities for each player
    :param piece_type: the unit of currency the players are using
    :param pcs_in_pot: the total number of pieces in the pot
    :param total_piece_count: the number of pieces that must always be present
    """
    while len(players) > 1:
        pcs_in_pot, dummy = check(players, player_pieces, piece_type, pcs_in_pot, total_piece_count, 0)
        if len(players) > 1:
            # print player totals
            for i in range(len(players)):
                print(players[i] + ": " + str(player_pieces[i]) + " " + piece_type)

            print("\nEach player will now spin the dreidel.")
            i = 0
            while i < len(players):
                player_pieces[i], pcs_in_pot = spin(players[i], player_pieces[i], piece_type,
                                                    pcs_in_pot)
                pcs_in_pot, lower_index_elims = check(players, player_pieces, piece_type,
                                                      pcs_in_pot, total_piece_count, i)
                # shift the list while accounting for players w/ earlier turns leaving
                i -= lower_index_elims
                i += 1

            if len(players) > 1:
                print("\nThe round has ended.\n"
                      "Each player will now add one of their " + piece_type +
                      " to the pot.")
                for i in range(len(players)):
                    player_pieces[i] -= 1
                    pcs_in_pot += 1

                print("Current Pot Total: " + str(pcs_in_pot) + " " + piece_type)
                print("[Press any key to continue]")
                input()


def new_game(num_players, piece_type, pcs_per_player, total_piece_count):
    """
    Initiate a series of rounds until the game ends
    :param num_players: the number of players at the start of the game
    :param piece_type: the unit of currency the players are using
    :param pcs_per_player: the number of pieces each player starts with
    :param total_piece_count: the number of pieces that must always be present
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

    print("[Press any key to continue]")
    input()

    # while len(players) > 1:
    #    new_round(players, player_pieces, piece_type, pcs_in_pot, total_piece_count)

    play_rounds(players, player_pieces, piece_type, pcs_in_pot, total_piece_count)


def main():
    """
    Set up the players and pieces and start a new game
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
                       " (ex. candy bars, dollars)\n"
                       "(Please answer in the plural form) \n")

    # set the number of pieces each player starts with
    pcs_per_player = int(input("How many " + piece_type +
                               " each would you like to play with? \n"))
    while pcs_per_player < 2:
        pcs_per_player = int(
            input("How many " + piece_type + " would you like to play with?"
                                             "\n(Must be an integer greater than 1) \n"))

    # the number of pieces that must always be present
    total_piece_count = num_players * pcs_per_player

    new_game(num_players, piece_type, pcs_per_player, total_piece_count)


if __name__ == "__main__":
    main()
