## Play tic tac toe
first_row = ['a', 'b', 'c']
second_row = ['d','e','f']
third_row = ['g','h','i']


def check_for_winner(array_1, array_2, array_3, xo, player):
    # Check for Straight Line
    if (array_1 == [xo,xo,xo]) | (array_2 == [xo,xo,xo]) | (array_3 == [xo,xo,xo]) | (array_1[0] == xo and array_2[0] == xo and array_3[0] == xo) | (array_1[1] == xo and array_2[1] == xo and array_3[1] == xo | (array_1[2] == xo and array_2[2] == xo and array_3[2] == xo) | (array_1[0] == xo and array_2[1] == xo and array_3[2] == xo) | (array_1[2] == xo and array_2[1] == xo and array_3[0] == xo)):
        print(f'{player} Wins!!')
        return False
    # Check for Diagnal
    if (array_1[0] == xo and array_2[1] == xo and array_3[2] == xo) | (array_1[2] == xo and array_2[1] == xo and array_3[0] == xo):
        print(f'{player} Wins!!')
        return False
    else:
        return True

def change_players(player):
    if player == 'Player_1':
        player = 'Player_2'
        return player
    else:
        player = 'Player_1'
        return player

game_on = True
player = 'Player_1'
print(first_row)
print(second_row)
print(third_row)
while game_on:
    
    current_move = str(input(f'{player} - Select where you would like to make your move: '))

    if player == 'Player_1':
        xo = 'X'
    else:
        xo = 'O'


    if current_move in first_row:
        move_index = first_row.index(current_move)
        first_row[move_index] = xo
        print(first_row)
        print(second_row)
        print(third_row)
        game_on = check_for_winner(first_row, second_row, third_row, xo, player)
        player = change_players(player)
        
    elif current_move in second_row:
        move_index = second_row.index(current_move)
        second_row[move_index] = xo
        print(first_row)
        print(second_row)
        print(third_row)
        game_on = check_for_winner(first_row, second_row, third_row, xo, player)
        player = change_players(player)

    elif current_move in third_row:
        move_index = third_row.index(current_move)
        third_row[move_index] = xo
        print(first_row)
        print(second_row)
        print(third_row)
        game_on = check_for_winner(first_row, second_row, third_row, xo, player)
        player = change_players(player)

    else:
        print('You must pick an available space')
