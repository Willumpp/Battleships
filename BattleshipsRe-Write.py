"""
Project re-draft started: 18/09/21

The aim of this project is the improve some very old code of the text based game 'Battleships'
"""

import random

hit = []
player_hits = 0
enemy_hits = 0
rep = True

#Create the player's board
row = [' [ ] ' for column_i in range(10)] #Create 1 row, with 10 columns
players_board = [row.copy() for row_i in range(10)] #Create 10 of these rows and add to array
player_foreboard = players_board.copy()

#Create the enemy's board
enemys_board = [row.copy() for row_i in range(10)] #Create 10 of these rows and add to array


#Display a given board
#   loop through each row, printing the row number and all columns
def display_board(board):
    #Loop through each row of the board
    for row_i, row in enumerate(board):
        #Display the row number, starting from 10, descending
        #display the row after
        #also use a "tab" indent
        print(str(len(board)-row_i)+"\t", "".join(row))

    #x-axis
    print("\t   1    2    3    4    5    6    7    8    9   10")


#Add ships to board
#Top Row, 2 Long, Horizontal
p_rng = random.randint(0,8)
e_rng = random.randint(0,8)
for column_i in range(0, 2):
    players_board[9][p_rng+column_i] = ' [:] '
    enemys_board[9][e_rng+column_i] = ' [:] '

#9th Row, 4 Long, Vertical
p_rng = random.randint(0,9)
e_rng = random.randint(0,9)
for row_i in range(5, 9):
    players_board[row_i][p_rng] = ' [:] '
    enemys_board[row_i][e_rng] = ' [:] '

#5th Row, 3 Long, Horizontal
p_rng = random.randint(0,6)
e_rng = random.randint(0,6)
for column_i in range(0, 3):
    players_board[4][p_rng+column_i] = ' [:] '
    enemys_board[4][e_rng+column_i] = ' [:] '

#3rd Row, 2 Long, Vertical
p_rng = random.randint(0,9)
e_rng = random.randint(0,9)
for row_i in range(1, 3):
    players_board[row_i][p_rng] = ' [:] '
    enemys_board[row_i][e_rng] = ' [:] '

#1st Row, 1 Long
p_rng = random.randint(0,9)
e_rng = random.randint(0,9)
players_board[0][p_rng] = ' [:] '
enemys_board[0][e_rng] = ' [:] '


#Display what each character means
print('''
[ ] = Empty cell
[:] = Ship occupies cell

[-] = Miss
[_] = Miss and if miss overlaps with owned occupied cell
[*] = Successful hit
[^] = Successful hit and if hit overlaps with owned occupied cell
[/] = Ship cell sunk
[\] = Ship cell sunk but also a hit on enemy
''')

ship_cells = [" [:] ", " [_] ", " [^] ", " [\] "]

while rep == True:
    #Draw Board 
    display_board(player_foreboard)
    
    for i in range(5):
     
        #Ask for player's co-ordinates
        #"p" = "player"
        p_column = -1
        p_row = -1
        #Use these while loops to avoid guessing outside the range of the array
        while p_column < 0 or p_column > 9:
            p_column = int(input('Which column do you want to choose?')) - 1
        while p_row < 0 or p_row > 9:
            p_row = 10 - int(input('Which row do you want to choose?'))
        
        #Find CPU Coordinates
        #"e" = "enemy"
        e_column = random.randint(0,9)
        e_row = random.randint(0,9)

        #Player guess handling
        #If successful hit on enemy
        if enemys_board[p_row][p_column] == " [:] ":
            player_hits += 1 #Increment player's score

            #Need to mark the enemy's board
            #otherwise, the player can guess the same spot twice
            enemys_board[p_row][p_column] = " [/] "

            #If guesses location overlaps with player ship
            if player_foreboard[p_row][p_column] in ship_cells:
                player_foreboard[p_row][p_column] = " [^] " #Mark as hit and owned ship
            else:
                player_foreboard[p_row][p_column] = " [*] " #Mark as hit but no owned ship
        else: #Miss
            #If miss location overlaps with player ship
            if player_foreboard[p_row][p_column] in ship_cells:
                player_foreboard[p_row][p_column] = " [_] " #Mark as miss and owned ship
            else:
                player_foreboard[p_row][p_column] = " [-] " #Mark as miss but no owned ship



        #Enemy guess handling
        #If successful hit on player
        if players_board[e_row][e_column] == " [:] ":
            enemy_hits += 1

            #Need to mark the player's board
            #otherwise, the enemy can guess the same spot twice
            players_board[p_row][p_column] = " [/] "

            #If hit marker overlaps with player ship
            if player_foreboard[e_row][e_column] in ship_cells:
                player_foreboard[e_row][e_column] = " [\] " #Mark sink and owned ship
            else:
                player_foreboard[e_row][e_column] = " [/] " #Mark sing and no owned ship


    #Test Which Side Wins
    # There are 12 cells available to sink on either side
    if player_hits >= 12:
        print("PLAYER WINS!!!")
        rep = False
    
    if enemy_hits >= 12:
        print("ENEMY WINS!!!")
        rep = False