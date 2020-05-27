import numpy
playercount = 0
game = numpy.array([[0, 0, 0],
                   [0, 0, 0],
                    [0, 0, 0]])

print("Player 1 is X Player 2 is O")
if playercount == 0:
    playercount += 1


def whosgo():
    mod = playercount % 2
    if mod > 0:
        print("it's player 1's turn")
    else:
        print("it's player 2's turn, O's")


def createboard():
    tcolumns = "    |   " * 2
    print(tcolumns)
    rows = " ---------------"
    print(rows)
    print(tcolumns)
    print(rows)
    print(tcolumns)


def newgame():
    playercount = 0
    row = int(input("what row do you want to go in? "))
    column = int(input("and what column? "))
    rows = " ---------------"
    tcolumns = "    |   " * 2
    if row == 1 and column == 1:
        print("  X |       |    ")
        print(rows)
        print(tcolumns)
        print(rows)
        print(tcolumns)
        playercount += 1
    elif row == 2 and column == 1:
        print(tcolumns)
        print(rows)
        print("  X |       |    ")
        print(rows)
        print(tcolumns)
    elif row == 3 and column == 1:
        print(tcolumns)
        print(rows)
        print(tcolumns)
        print(rows)
        print("  X |       |    ")
    elif row == 2 and column == 2:
        print("  X |   O   |    ")
        print(rows)
        print("    |   X   |    ")
        print(rows)
        print(tcolumns)
        playercount += 1

    print(game[1])


def player2():
    print("it's player 2's turn")
    playercount = 1
    row = int(input("what row do you want to go in? "))
    column = int(input("and what column? "))
    rows = " ---------------"
    tcolumns = "    |   " * 2
    if game == [[1, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]:
        print("  X |       |    ")
    if int(row) == 1 and int(column) == 2:
        game.insert(1, game[2])
        print("  X |   O   |    ")
        print(rows)
        print(tcolumns)
        print(rows)
        print(tcolumns)
        playercount += 1
    elif row == 2 and column == 2:
        game.insert(1, game[2])
        print("  O |      |    ")
        print(rows)
        print(tcolumns)
        print(rows)
        print(tcolumns)
        playercount += 1
    # print(playercount)


def whowon():
    winner_is_2 = [[2, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]

    winner_is_2d = [[2, 2, 2],
                    [2, 1, 0],
                    [0, 1, 1]]

    winner_is_1 = [[1, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]
    no_winner = [[1, 2, 0],
                 [2, 1, 0],
                 [2, 1, 2]]

    also_no_winner = [[1, 2, 0],
                      [2, 1, 0],
                      [2, 1, 0]]
    if game == winner_is_2:
        print("congrats X wins!!")
    elif game == winner_is_2d:
        print("congrats X wins!")
    elif game == winner_is_1:
        print("congrats O wins!!")
    elif no_winner == game:
        print("it's a tie!!")
    elif also_no_winner == game:
        print("it's a tie!!")
    while game != winner_is_2 and game != winner_is_2d and game != winner_is_1 and game != no_winner and \
            game != also_no_winner:
        whosgo()
        newgame()
        player2()


createboard()
whowon()
