import random


def guessgame():
    number = random.randrange(0, 10)
    guess = 0

    while guess != "quit" and guess != number:
        guess = input("guess my number asshole: ")
        if int(guess) > number:
            print("too big dickbreath")
        elif int(guess) < number:
            print("aim higher ya piss poor prostitute")
        elif int(guess) == number:
            print("well done smelly tits you actually got something right!")
            break
        elif guess == "quit":
            break


guessgame()
