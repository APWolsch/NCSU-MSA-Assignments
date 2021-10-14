# Define Board
TheGrid = {'A1': ' ', 'B1': ' ', 'C1': ' ',
           'A2': ' ', 'B2': ' ', 'C2': ' ',
           'A3': ' ', 'B3': ' ', 'C3': ' '}


def printBoard(board):
    print(board['A1'] + '|' + board['B1'] + '|' + board['C1'])
    print('-+-+-')
    print(board['A2'] + '|' + board['B2'] + '|' + board['C2'])
    print('-+-+-')
    print(board['A3'] + '|' + board['B3'] + '|' + board['C3'])


def game():
    turn = 'X'
    count = 0
    position = input("Choose a position: ")
    print(position)

    for i in range(10):
        printBoard(TheGrid)
        if TheGrid[position] == ' ':
            TheGrid[position] = turn
            count += 1
        else:
            print("You can't go here.  It's already taken.\nEnter another place?")
            continue
        if count >= 5:
            if TheGrid['A1'] == TheGrid['A2'] == TheGrid['A3'] != ' ':  # across the top
                printBoard(TheGrid)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
