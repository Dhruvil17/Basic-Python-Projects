import random
randomNumber = random.randrange(1,10)
userGuess = int(input("Enter any number : "))

while randomNumber != userGuess:
    if userGuess < randomNumber:
        print("Number guessed is smaller than actual number. Guess any larger number\n")
        userGuess = int(input("Enter any other number : "))
    elif userGuess > randomNumber:
        print("Number guessed is larger than actual number. Guess any smaller number\n")
        userGuess = int(input("Enter any other number : "))
    else:
        break

print("Hurray ! You have guessed the correct number.")
