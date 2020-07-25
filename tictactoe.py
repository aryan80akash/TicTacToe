# board
# display board
# play game
# handle game
# check win
# check rows
# check columns
# check diagonals
# check tie
# flip player


# --- Global Variables
# If game is still going
game_still_going = True

# Who won or Tie?
winner = None

# Who's Turn is it
current_player = "X"

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]


# Display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# defining a menu


# def menu():
    # Play Against another player
    # play against computer
    # Quit


# Play a Game of Tic Tac Toe
def play_game():
    # Display the inital board
    display_board()

    while game_still_going:

        # Handle a Single turn of an arbitary player
        handle_turn(current_player)
        # Check if game has ended
        check_if_game_over()
        # flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print("Booyah! " + winner + " Won.")
    elif winner == None:
        print("And Tie It is.")


# Handle a Single Turn of an arbitarary player
def handle_turn(player):
    position = input(
        "[" + player + "'s Turn] Choose a Position from 1-9: ")

    valid = False

    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input(
                "Invalid Position, Please Try Again.\n" "[" + player + "'s Turn] Choose a Position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there.")
            display_board()

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # set up global winner
    global winner
    # check Rows
    row_winner = check_rows()
    # check Columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    # set up global variable
    global game_still_going

    # check if any of the rows have all the same values (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row there's a match, flag that there's win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return


def check_columns():
    # set up global variable
    global game_still_going

    # check if any of the columns have all the same values (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column there's a match, flag that there's win
    if column_1 or column_2 or column_3:
        game_still_going = False

        # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return


def check_diagonals():
    # set up global variable
    global game_still_going

    # check if any of the diagonals have all the same values (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If any diagonal there's a match, flag that there's win
    if diagonal_1 or diagonal_2:
        game_still_going = False

        # Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    return


def check_if_tie():
    # Set up global Varible
    global game_still_going
    # Check if there's Tie
    if "-" not in board:
        game_still_going = False

    return


def flip_player():
    # Set up global Varible
    global current_player
    # If Current player is X change it to O and Vice-Versa
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return


play_game()
