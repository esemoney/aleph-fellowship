# first I create a list of the gameboard positions then I convert it to a
# dictionary to so i can assign values to the positions

positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

game_board = dict.fromkeys(positions, " ")


# then a function to print out the board

def display_board():
    print(game_board[1] + "|" + game_board[2] + "|" + game_board[3])
    print("_ _ _")
    print(game_board[4] + "|" + game_board[5] + "|" + game_board[6])
    print("_ _ _")
    print(game_board[7] + "|" + game_board[8] + "|" + game_board[9])
    print("\n")


# function to check if the space on the board is occupied

def check_space(position):
    if game_board[position] == ' ':
        return True
    else:
        return False # the winning conditions are shown here
def check_for_win():
    if (game_board[1] == game_board[2] and game_board[1] == game_board[3] and game_board[1] != ' '):
        return True
    elif (game_board[4] == game_board[5] and game_board[4] == game_board[6] and game_board[4] != ' '):
        return True
    elif (game_board[7] == game_board[8] and game_board[7] == game_board[9] and game_board[7] != ' '):
        return True
    elif (game_board[1] == game_board[4] and game_board[1] == game_board[7] and game_board[1] != ' '):
        return True
    elif (game_board[2] == game_board[5] and game_board[2] == game_board[8] and game_board[2] != ' '):
        return True
    elif (game_board[3] == game_board[6] and game_board[3] == game_board[9] and game_board[3] != ' '):
        return True
    elif (game_board[1] == game_board[5] and game_board[1] == game_board[9] and game_board[1] != ' '):
        return True
    elif (game_board[7] == game_board[5] and game_board[7] == game_board[3] and game_board[7] != ' '):
        return True
    else:
        return False


def check_which_mark_won(mark):
    if game_board[1] == game_board[2] and game_board[1] == game_board[3] and game_board[1] == mark:
        return True
    elif (game_board[4] == game_board[5] and game_board[4] == game_board[6] and game_board[4] == mark):
        return True
    elif (game_board[7] == game_board[8] and game_board[7] == game_board[9] and game_board[7] == mark):
        return True
    elif (game_board[1] == game_board[4] and game_board[1] == game_board[7] and game_board[1] == mark):
        return True
    elif (game_board[2] == game_board[5] and game_board[2] == game_board[8] and game_board[2] == mark):
        return True
    elif (game_board[3] == game_board[6] and game_board[3] == game_board[9] and game_board[3] == mark):
        return True
    elif (game_board[1] == game_board[5] and game_board[1] == game_board[9] and game_board[1] == mark):
                return True
    elif (game_board[7] == game_board[5] and game_board[7] == game_board[3] and game_board[7] == mark):
        return True
    else:
        return False

def check_for_draw():
    for key in game_board.keys():
        if (game_board[key] == ' '):
            return False
    return True


def player_move():
    position = int(input("Enter the position for 'O':  "))
    insert_letter(player, position)
    return

def insert_letter(letter, position):
    if check_space(position) == True:
        game_board[
            position] = letter
        display_board()

        if (check_for_draw()):
            print("Draw!")
            exit()
        if check_for_win():
            if letter == 'X':
                print("I win!")
                exit()
            else:
                print("Player wins!")
                exit()

        return


    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return




# i use the minimax algorithm to optimize the computer's gameplay so the computer either wins or draws
def comp_move():
    best_score = -800
    best_move = 0
    for key in game_board.keys():
        if (game_board[key] == ' '):
            game_board[key] = computer
            score = minimax(game_board, 0, False)
            game_board[key] = ' '
            if (score > best_score):
                best_score = score
                best_move = key

    insert_letter(computer, best_move)
    return


def minimax(game_board, depth, is_maximizing):
    if (check_which_mark_won(computer)):
        return 1
    elif (check_which_mark_won(player)):
        return -1
    elif (check_for_draw()):
        return 0

    if (is_maximizing):
        best_score = -800
        for key in game_board.keys():
            if (game_board[key] == ' '):
                game_board[key] = computer
                score = minimax(game_board, depth + 1, False)
                game_board[key] = ' '
                if (score > best_score):
                    best_score = score
        return best_score

    else:
        best_score = 800
        for key in game_board.keys():
            if (game_board[key] == ' '):
                game_board[key] = player
                score = minimax(game_board, depth + 1, True)
                game_board[key] = ' '
                if (score < best_score):
                    best_score = score
        return best_score



print("Welcome to my Tic Tac Toe game!")
print("I play the 'X' and I always go first. You can't beat me but I'd love to see you try.")
print("Here are the positions. Enter the number of the position you'd like to play in.")
print("1, 2, 3")
print("4, 5, 6")
print("7, 8, 9")
print("\n")
player = "O"
computer = "X"
game_board[5] = "X"
display_board()
print("Your turn")
player_move()


while not check_for_win():
    player_move()
    comp_move()
