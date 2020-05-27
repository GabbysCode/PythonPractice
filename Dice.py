import random
choice = input("what game would you like to play? Rock paper scissors or rolling dice? ")

def again():
    rematch = input("you wanna play again? yes or no? ")
    y = "yes"
    n = "no"
    if rematch == y:
        if choice == "dice":
            dice()
        elif choice == "rock paper scissors":
            rockpaperscissors()
    elif rematch == n:
        print("play again soon!")
    else:
        print("uhh...that's not an answer buddy")
        again()

def dice():
    number = random.randrange(1, 7)
    if number == 6:
        print("you rolled a 6, yay you! you start the game first!")
        winner()
    elif number < 6:
        print("you rolled a " + str(number) + " try for a 6!")
        again()


def winner():
        other = input("do you wanna play a different game? ")
        if other == "yes" and choice == "dice":
            rockpaperscissors()
        elif other == "yes" and choice == "rock paper scissors":
            dice()
        elif other == "no":
            replay = input("do you want to play another game of " + choice + "?")
            if replay == "yes":
                if choice == "rock paper scissors":
                    rockpaperscissors()
                elif choice == "dice":
                    dice()
            elif replay == "no":
                print("play again sometime soon!")

    # if number < 6:
    #     again()

# while number < 6:
#     dice()
#     break


def rockpaperscissors():
    hand = ["rock", "paper", "scissors"]

    play = random.choice(hand)
    player = input("Rock, Paper, Scissors? ")
    print("I play " + play)
    print("**" * 18)

    if player == play:
        print("we picked the same thing...")
        rockpaperscissors()

    elif player == "rock" and play == "paper":
        print("paper covers rock I win!")

    elif player == "paper" and play == "rock":
        print("paper covers rock you win!")

    elif player == "rock" and play == "scissors":
        print("rock beats scissors you win!")

    elif player == "scissors" and play == "rock":
        print("scissors beats rock I win!")

    elif player == "paper" and play == "scissors":
        print("paper is cut by scissors I win!")

    elif player == "scissors" and play == "paper":
        print("scissors cut up paper you win!")
    again()


if choice.lower() == "rock paper scissors":
    rockpaperscissors()
elif choice.lower() == "dice":
    dice()


def whatgame():
    choose = input("what game do you wanna play? ")
    choice = choose
    if choice == "dice":
        dice()
    elif choice == "rock paper scissors":
        rockpaperscissors()


#] whatgame()

