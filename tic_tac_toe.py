# Making a TIC-TAC-TOE game from scratch in python

import random
import os

# global constants for Player1 and Player2
p1 = "Player1"
p2 = "Player2"


def clear_screen() -> None:
    """
    Clears the screen using the appropriate command for the operating system.
    If running in an IDE (like PyCharm), it simply prints new lines.
    """
    if os.getenv("PYCHARM_HOSTED") or "TERM" not in os.environ:
        # In PyCharm or IDE, print new lines instead of clearing the screen
        print("\n" * 50)
    else:
        # In a real terminal, clear the screen
        os.system("cls" if os.name == "nt" else "clear")


def display_board(board):
    """
    Displays the Tic Tac Toe board.

    Parameters:
    board (list): The current state of the Tic Tac Toe board.
    """
    clear_screen()
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])


def player_input():
    """
    Takes player input for marker selection (X or O).

    Returns:
    tuple: A tuple containing the markers chosen by Player 1 and Player 2.
    """
    marker = "wrong"  # initially assume that input is wrong

    while marker not in ["X", "O"]:
        marker = input("Player 1, choose X or O: ").upper()
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    """
    Places the player's marker (X or O) at the specified position on the board.

    Parameters:
    board (list): The current state of the Tic Tac Toe board.
    marker (str): The marker to be placed (X or O).
    position (int): The position on the board where the marker will be placed.
    """

    board[position] = marker


def game_win_check(board, mark):
    """
    Checks if a player has won the game.

    Parameters:
    board (list): The current state of the Tic Tac Toe board.
    mark (str): The marker (X or O) to check for winning combinations.

    Returns:
    bool: True if the player with the specified marker has won, False otherwise.
    """
    return (
        (board[1] == mark and board[2] == mark and board[3] == mark)  # top row check
        or (
            board[4] == mark and board[5] == mark and board[6] == mark
        )  # middle row check
        or (
            board[7] == mark and board[8] == mark and board[9] == mark
        )  # bottom row check
        or (
            board[1] == mark and board[4] == mark and board[7] == mark
        )  # first column check
        or (
            board[2] == mark and board[5] == mark and board[8] == mark
        )  # second column check
        or (
            board[3] == mark and board[6] == mark and board[9] == mark
        )  # third column check
        or (
            board[1] == mark and board[5] == mark and board[9] == mark
        )  # first diagonal check
        or (board[3] == mark and board[5] == mark and board[7] == mark)
    )  # second diagonal check


def player_choice():
    """
    Randomly selects which player will go first.

    Returns:
    str: Either p1:'Player 1' or p2:'Player 2'.
    """
    if random.randint(0, 1) == 0:
        return p2
    else:
        return p1


def space_check(board, position):
    """
    Checks if a space on the board is empty.

    Parameters:
    board (list): The current state of the Tic Tac Toe board.
    position (int): The position on the board to check.

    Returns:
    bool: True if the space is empty, False otherwise.
    """
    return board[position] == " "


def full_board_check(board):
    """
    Checks if the Tic Tac Toe board is full.

    Parameters:
    board (list): The current state of the Tic Tac Toe board.

    Returns:
    bool: True if the board is full, False otherwise.
    """
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_next_position(board):
    """
    Prompts the player to choose the next position on the board.

    Parameters:
    board (list): The current state of the Tic Tac Toe board.

    Returns:
    int: The position chosen by the player.
    """

    position = 0  # assume it is out of the board

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Please choose your next position from 1-9: "))
    return position


def game_continue():
    """
    Asks the player if they want to continue playing the game.

    Returns:
    bool: True if the player wants to continue, False otherwise.
    """
    choice = "wrong"  # initially assume it is wrong

    while choice not in ["Y", "N"]:
        choice = input("Would you like to play again? (y/n): ").upper()

    return choice == "Y"


def main() -> None:
    print("Welcome to Tic Tac Toe!")

    while True:
        game_board = [" "] * 10  # reset the game board
        player1_marker, player2_marker = player_input()  # get player input
        turn = player_choice()  # check whose turn it is
        print(turn + " Will go first!")  # display which player will go first

        confirm = "wrong"
        while confirm not in ["Y", "N"]:
            confirm = input("Are you ready to play? (y/n): ").upper()

        if confirm == "Y":
            game_on = True
        elif confirm == "N":
            game_on = False

        while game_on:
            if turn == p1:  # player 1's turn
                display_board(game_board)  # display game board
                position = player_next_position(
                    game_board
                )  # ask player for next position if space empty
                place_marker(
                    game_board, player1_marker, position
                )  # place player's marker in the board

                if game_win_check(
                    game_board, player1_marker
                ):  # check if player1 wins the game
                    display_board(game_board)
                    print("Congratulations! Player 1 WINS!")
                    game_on = False
                else:  # check if the game is tied
                    if full_board_check(game_board):
                        display_board(game_board)
                        print("The Game is DRAW!")
                        break
                    else:
                        turn = p2  # if game not tied then back to player 2's turn

            else:  # player 2's turn
                display_board(game_board)  # display game board
                position = player_next_position(
                    game_board
                )  # ask player for next position if space empty
                place_marker(
                    game_board, player2_marker, position
                )  # place player's marker in the board

                if game_win_check(
                    game_board, player2_marker
                ):  # check if player2 wins the game
                    display_board(game_board)
                    print("Congratulations! Player 2 WINS!")
                    game_on = False
                else:  # check if the game is tied
                    if full_board_check(game_board):
                        display_board(game_board)
                        print("The Game is DRAW!")
                        break
                    else:
                        turn = p1  # if game not tied then back to player 1's turn

        if not game_continue():  # exit the game
            print("Thank you for playing! Exiting the Game......")
            break


# Main driver code
if __name__ == "__main__":
    main()
