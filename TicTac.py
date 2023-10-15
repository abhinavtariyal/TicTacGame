# -*- coding: utf-8 -*-


def displayBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])


def player_input():
    marker = ""
    while marker not in ["X", "O"]:
        marker = input("Please Pick a marker X or O\n").upper()
    player1 = marker
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    return (player1, player2)


def get_position():
    pos = ""
    validRange = False
    while not pos.isdigit() or not validRange:
        pos = input("Enter the position you want to place the marker ")
        if pos.isdigit():
            if int(pos) in range(1, 10):
                validRange = True
                break
            else:
                print("Not in Range, please try again ")
                continue
        else:
            print("Enter a valid position")
    return int(pos)


def place_marker(board, marker, position):
    board[position] = marker
    return board


def console():
    while True:
        placesFilled = []
        testBoard = [" "] * 10
        displayBoard(testBoard)
        (player1, player2) = player_input()
        marker = player1
        while True:
            position = get_position()
            if position in placesFilled:
                print("Sorry, position already taken, please select another position")
                continue
            testBoard = place_marker(testBoard, marker, position)

            if (
                testBoard[7] == testBoard[8] == testBoard[9] == marker
                or testBoard[1] == testBoard[2] == testBoard[3] == marker
                or testBoard[4] == testBoard[5] == testBoard[6] == marker
                or testBoard[1] == testBoard[4] == testBoard[7] == marker
                or testBoard[2] == testBoard[5] == testBoard[8] == marker
                or testBoard[3] == testBoard[6] == testBoard[9] == marker
                or testBoard[1] == testBoard[5] == testBoard[9] == marker
                or testBoard[3] == testBoard[5] == testBoard[7] == marker
            ):
                print(f"Player with {marker} marker has won")
                break

            placesFilled.append(position)
            displayBoard(testBoard)
            if marker == "X":
                marker = "O"
            else:
                marker = "X"
        choice = "default"
        while choice not in ["Y", "N"]:
            choice = input(
                "Enter Y if you want to continue playing, N if you want to quit "
            ).upper()
        if choice == "Y":
            continue
        else:
            print("The Game has ended, Thanks for playing!!!")
            break

console()
