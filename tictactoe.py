def get_position(board):

    #keep asking if position is not free
    position = int(input("Choose your next position: (1-9): "))
    #print("you chose: {}".format(position))
    while space_check(board,position) != True:
            position = int(input("Position is occupied. Choose another position: (1-9): "))
    return position

def space_check(board,position):
    #return True if position is free
    return board[position] == ' '

def check_win(board,mark):
     if ((board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or \
        (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or \
        (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or \
        (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark)):
         return True
     else:
        return False
#from IPython.display import clear_output
import os
# for windows
def clear_output():
    os.system('clear')

#def clear_output():
#    os.system( 'cls' )
def display_board(board):
    clear_output()
    print(board[7] + ' | ' + board[8] +' | '+ board[9])
    print('---------')
    print( board[4] +' | '+ board[5]+' | '+ board[6])
    print('---------')
    print(board[1] +' | '+ board[2] +' | '+ board[3])

def  check_full(board):
    for i in range(1,10) :
        if board[i] == ' ':
            return False
    return True

def repeat():
    repeat = ' '
    while not (repeat == 'y' or repeat == 'n' ):
            repeat = input("Would you like to repeat the game? y or n: ")

    if repeat == 'y':
        return True
    else:
        return False

import random
def choose_first():
    if  random.randint(0,1) == 0:
            return 'player1'
    else:
            return 'player2'

def get_input():
    choice = ' '
    while not (choice.upper() == 'X' or choice.upper() == 'O'):
        choice = str(input("Player1 Choose X or O: "))
    return choice.upper()

def check_ready():
    ready = ' '
    while not (ready.lower() == 'y' or ready.lower() == 'n'):
        ready = str(input("Are you ready to play: y or n "))

    if ready == 'y':
        return True
    else:
        return False

def place_marker(board, marker, position):
    board[position] = marker

#Tic Tac Toe
print("Welcome to Tic Tac Toe")
# Run the game on start
while True:

    # Ask for player marker choice
    player1 =  get_input()
    # Assigned marker to player 2
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    # Choose who will begin first
    who_start = choose_first()

    print(who_start + " will begin")
    # Ask if ready to play
    play = check_ready()
    board = [' ']*10
    # Start playing
    while play:
        # board
        display_board(board)
        # player 1

        if who_start == 'player1':
            # Ask for position
            position = get_position(board)
            place_marker(board, player1, position)
            if check_win(board,player1):
                display_board(board)
                print("Player 1 won! ")
                play = False
                break
            elif check_full(board):
                display_board(board)
                print("*** It's a tie! *****")
                play = False
                break
            else:
                who_start = 'player2'
                    # check if player 1 won
                    # check if board is full
                    # player 2 turn
        else:
              #player 2

                    # Ask for position
            position = get_position(board)
            place_marker(board, player2, position)
            if check_win(board,player2):
                display_board(board)

                print("Player 2 won! ")
                play = False
            elif check_full(board):
                display_board(board)

                print("*** It's a tie! *****")
                play = False
            else:
                 who_start = 'player1'
                    # check if position is free
                    # check if player 1 won
                    # check if board is full
                    # player 2 turn
    if repeat():
        clear_output()
        pass
    else:
        break
