# setting global matrix to represent the game board - all functions will use
mat_of_tuples = [[0] * 3 for i in range(0, 3)]


def decide_win():
    """
    checking whether the board contains a winning sequel for one of the symbols
    :return: boolean value to indicate whether the game is over
    """
    if mat_of_tuples[0][0] != 0 and mat_of_tuples[0][0] == mat_of_tuples[0][1] == mat_of_tuples[0][2]:
        return True
    if mat_of_tuples[1][0] != 0 and mat_of_tuples[1][0] == mat_of_tuples[1][1] == mat_of_tuples[1][2]:
        return True
    if mat_of_tuples[2][0] != 0 and mat_of_tuples[2][0] == mat_of_tuples[2][1] == mat_of_tuples[2][2]:
        return True
    if mat_of_tuples[0][0] != 0 and mat_of_tuples[0][0] == mat_of_tuples[1][0] == mat_of_tuples[2][0]:
        return True
    if mat_of_tuples[0][1] != 0 and mat_of_tuples[0][1] == mat_of_tuples[1][1] == mat_of_tuples[2][1]:
        return True
    if mat_of_tuples[0][2] != 0 and mat_of_tuples[0][2] == mat_of_tuples[1][2] == mat_of_tuples[2][2]:
        return True
    if mat_of_tuples[0][0] != 0 and mat_of_tuples[0][0] == mat_of_tuples[1][1] == mat_of_tuples[2][2]:
        return True
    if mat_of_tuples[0][2] != 0 and mat_of_tuples[0][2] == mat_of_tuples[1][1] == mat_of_tuples[2][0]:
        return True
    return False


def set_board(location_tuple, type_of_symbol):
    """
setting the symbol in an asked position represented as tuple, if the location already has a symbol inside it - making the user choose another location
    :param location_tuple: asked location for the symbol
    :param type_of_symbol: which symbol are we using
    :return: none
    """
    # in case there are no symbol in this cell
    if mat_of_tuples[location_tuple[0] - 1][location_tuple[1] - 1] == 0:
        mat_of_tuples[location_tuple[0] - 1][location_tuple[1] - 1] = (ord(type_of_symbol))
    # in case there is
    else:
        while mat_of_tuples[location_tuple[0] - 1][location_tuple[1] - 1] != 0:
            # let the user know
            print('the tuple: ', location_tuple, 'is already containing the symbol',
                  chr(mat_of_tuples[location_tuple[0] - 1][location_tuple[1] - 1]))
            # take another input - until the input is correct
            location_tuple = get_location_of_play()
            # set it in matrix
        mat_of_tuples[location_tuple[0] - 1][location_tuple[1] - 1] = (ord(type_of_symbol))
    print_board()


def print_board():
    """
    printing the game board with all symbols
    :return: none
    """
    for list in mat_of_tuples:
        for number in list:
            if number == 0:
                print(' * ', end='')
                print(' ', end='')
            else:
                print(' ' + chr(number) + ' ', end='')
                print(' ', end='')
        print('')


def decide_sec_symbol(starting_symbol):
    """
    return the opposite symbol for the second player
    :param starting_symbol: the symbol chosen to start
    :return: none
    """
    if str(starting_symbol) == 'X':
        return 'O'
    else:
        return 'X'


def receive_starting_symbol():
    """
    receive's the starting symbol from user and decide the second one
    :return: none
    """
    starting_symbol = input('WELCOME TO TIC TAC TOW\n please choose starting symbol (X or O)')
    while starting_symbol != 'X' and starting_symbol != 'O':
        starting_symbol = input('ERROR: THE SYMBOL CHOSEN IS WRONG YOU CAN USE ONLY: (X or O)')
    sec_symbol = decide_sec_symbol(starting_symbol)
    return_tuple = (starting_symbol, sec_symbol)
    return return_tuple


def get_location_of_play():
    """
    gets the position of next move from the user, validate it and return it as tuple
    :return: tuple version of string input
    """
    location_string = input('enter the location of your move as a tuple')
    location_tuple = tuple(int(x) for x in location_string.split(","))
    while location_tuple[0] > 3 or location_tuple[0] < 0 or location_tuple[1] > 3 or location_tuple[1] < 0:
        location_string = input(
            'ERROR: location tuple has to be between [1,1] to [3,3], please enter new - valid location')
        location_tuple = tuple(int(x) for x in location_string.split(","))
    return location_tuple


################ main function################
def main():
    (starting_symbol, sec_symbol) = receive_starting_symbol()
    is_starting = True
    is_game_over = False
    while (not is_game_over):
        location_tuple = get_location_of_play()
        if is_starting:
            set_board(location_tuple, starting_symbol)
        else:
            set_board(location_tuple, sec_symbol)
        if decide_win():
            break
        else:
            is_starting = not is_starting
    if is_starting:
        print('WE GOT A WINNER!! the symbol: ', starting_symbol)
    else:
        print('WE GOT A WINNER!! the symbol: ', sec_symbol)


if __name__ == '__main__':
    main()
