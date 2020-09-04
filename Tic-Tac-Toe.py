box = [0,1,2,3,4,5,6,7,8,9]

def main():
    player = 1
    status = -1

    while status== -1:
        board()
        
        if player%2 == 1:
            player = 1
        else:
            player = 2

        print('\nPlayer', player)
        choice = int(input('Enter the position '))

        if player == 1:
            mark = 'X'
        else:
            mark = 'O'

        if choice == 1 and box[1] == 1:
            box[1] = mark
        elif choice == 2 and box[2] == 2:
            box[2] = mark
        elif choice == 3 and box[3] == 3:
            box[3] = mark
        elif choice == 4 and box[4] == 4:
            box[4] = mark
        elif choice == 5 and box[5] == 5:
            box[5] = mark
        elif choice == 6 and box[6] == 6:
            box[6] = mark
        elif choice == 7 and box[7] == 7:
            box[7] = mark
        elif choice == 8 and box[8] == 8:
            box[8] = mark
        elif choice == 9 and box[9] == 9:
            box[9] = mark
        else:
            print('Invalid move ')
            player -= 1
                
        status = game_status()
        player += 1
            
    print('RESULT')    
    if status == 1:
        print('Player',player-1,'win')
    else:
        print('Game draw')
 
def game_status():
    if box[1] == box[2] and box[2] == box[3]:
        return 1
    elif box[4] == box[5] and box[5] == box[6]:
        return 1
    elif box[7] == box[8] and box[8] == box[9]:
        return 1
    elif box[1] == box[4] and box[4] == box[7]:
        return 1
    elif box[2] == box[5] and box[5] == box[8]:
        return 1
    elif box[3] == box[6] and box[6] == box[9]:
        return 1
    elif box[1] == box[5] and box[5] == box[9]:
        return 1
    elif box[3] == box[5] and box[5] == box[7]:
        return 1
    elif box[1] != 1 and box[2] != 2 and box[3] != 3 and box[4] != 4 and box[5] != 5 and box[6] != 6 and box[7] != 7 and box[8] != 8 and box[9] != 9:
        return 0
    else:
        return -1
 
def board():
    print('\n\n\tTic Tac Toe\n\n')

    print('Player 1 (X)  -  Player 2 (O)' ) 
    print()

    print('     |     |     ' )
    print(' ' ,box[1] ,' | ' ,box[2] ,' |  ' ,box[3] )

    print('_____|_____|_____' )
    print('     |     |     ' )

    print(' ' ,box[4] ,' | ' ,box[5] ,' |  ' ,box[6] )

    print('_____|_____|_____' )
    print('     |     |     ' )

    print(' ' ,box[7] ,' | ' ,box[8] ,' |  ' ,box[9] )

    print('     |     |     ' )

main()