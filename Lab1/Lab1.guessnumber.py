import random

gameEnded = False
while gameEnded == False:
    print("Choose the game you want to play. Enter 1 to play with guessing numbers, enter 2 to play with "
          "Rock–paper–scissors or 3 to exit the game.")
    userChoice = int(input())
    if userChoice == 1:
        randomNumber = random.randrange(1, 21)
        print("A random number between 1 and 20 has been generated.")
        guessed = False
        while guessed == False:
            userNumber = int(input("Take a guess: "))
            if userNumber == randomNumber:
                guessed = True
                print("Excellent, Well done!")
            elif userNumber > randomNumber:
                print("Try once more, a bit lower")
            elif userNumber < randomNumber:
                print("Try once more, a bit higher")
        print("Yes, you found it!")
    elif userChoice == 2:
        randomNumber = random.randrange(1, 4)
        print("Rock–paper–scissors")
        guessed = False
        while guessed == False:
            userChoice = int(input("Choose 1 for Rock, 2 for Paper or 3 for Scissors."))
            if randomNumber == userChoice:
                print("Match is draw. Try again!")
            elif randomNumber == 1:
                if userChoice == 2:
                    print("You won! Computer choice: Rock.")
                if userChoice == 3:
                    print("You lost! Computer choice: Rock.")
                guessed = True
            elif randomNumber == 2:
                if userChoice == 1:
                    print("You lost! Computer choice: Paper.")
                if userChoice == 3:
                    print("You won! Computer choice: Paper.")
                guessed = True
            elif randomNumber == 3:
                if userChoice == 1:
                    print("You won! Computer choice: Scissors.")
                if userChoice == 2:
                    print("You lost! Computer choice: Scissors.")
                guessed = True
            else:
                print("Choose a number between 1, 2 and 3.")

    elif userChoice == 3:
        print("Game ended. Thank you for playing with us!")
        gameEnded = True
