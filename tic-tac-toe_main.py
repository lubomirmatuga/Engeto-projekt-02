# projekt_2.py: druhý projekt do Engeto Online Python Akademie

# author: Ľubomír Maťuga
# email: matugalubomir@gmail.com
# discord: Ľubomír Maťuga

# TIC-TAC-TOE

# IMPORT
from grid_creation import grid_creator
from grid_print import grid_printer

# GAME INTRODUCTION
print("""Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the NxN grid. The WINNER is
who succeeds in placing N of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game""")

# PLAYER SIGN SELECTION
while True:
    sign_1 = input("Choose sign for Player 1 (O or X): ").upper()
    print()
    if sign_1 == "O":
        sign_2 = "X"
        print("Player 1 has 'O' sign")
        print("Player 2 has 'X' sign")
        break
    elif sign_1 == "X":
        sign_2 = "O"
        print("Player 1 has 'X' sign")
        print("Player 2 has 'O' sign")
        break
    else:
        print ("Wrong input! Try again!")
print()

player_dict={"Player 1" : sign_1,
             "Player 2" : sign_2
             }

# SIZE OF GAMEBOARD SELECTION
while True:
    try:
        g = int(input("Enter size of gameboard: "))
        if g < 3:
            print ("Board is not big enough! Try again!")
        else:
            break
    except ValueError:
        print("Wrong input! Try again!")
    except NameError:
        print("Wrong input! Try again!")

# GAME
empty_sign = "_"
print("Initial state of",g,"x",g,"gameboard:")
game_board = (grid_creator(g,empty_sign))
grid_printer(game_board)  # Initial state
game_over = False  # Variable for end game checking
for round in range (1,2*g):
    print("Welcome in round:",round)
    for player, sign in player_dict.items():
        print("It is " + str(player) + " turn!")
        while True:
            try:
                while True:
                    x=(int(input("Enter your x coordinate:")))-1
                    if x in range (0,(g+1)):
                        break
                    else:
                        print("Wrong input! Try again!")
                while True:
                    y=(int(input("Enter your y coordinate:")))-1
                    if y in range (0,(g+1)):
                        break
                    else:
                        print("Wrong input! Try again!")
            except ValueError:
                print("Wrong input! Try again!")
            except NameError:
                print("Wrong input! Try again!")
            except IndexError:
                print("Wrong input! Try again!")
            if game_board[x][y]=="_":
                game_board[x][y]=sign
                grid_printer(game_board)
                print()
                break
            else:
                print("This cell is already occupied! Try again!")

# CHECKING RESULT
# COLUMNS
        for j in range (g):
            counter_column = 0
            for i in range (g):
                if game_board[i][j] == sign:
                    counter_column += 1
                    if counter_column == 3:
                        print (player + " win!")
                        game_over = True
                        break
# ROWS
        for j in range (g):
            counter_row = 0
            for i in range (g):
                if game_board[j][i] == sign:
                    counter_row += 1
                    if counter_row == 3:
                        print (player + " win!")
                        game_over = True
                        break
# RIGHT DIAGONAL
        counter_right_diag = 0
        for rd in range (g):
            if game_board[rd][rd] == sign:
                counter_right_diag += 1
                if counter_right_diag == 3:
                    print (player + " win!")
                    game_over = True
                    break
# LEFT DIAGONAL
        counter_left_diag = 0
        for ld in range (g):
            if game_board[ld][(g-ld-1)] == sign:
                counter_left_diag += 1
                if counter_left_diag == 3:
                    print (player + " win!")
                    game_over = True
                    break
# DRAW
        counter_draw=0
        for i in range (g):
            for j in range(g):
                if game_board[i][j] != empty_sign:
                    counter_draw += 1
                    if counter_draw == g*g:
                        print ("It is draw!")
                        game_over = True
                        break
            if game_over:
                    break
        if game_over:
            break
    if game_over:
        break