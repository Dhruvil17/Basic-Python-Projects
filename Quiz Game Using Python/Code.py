def userGuessCheck(userGuess, correctAnswer):
    global score
    stillGuessing = True
    attemptNumber = 1
    
    while stillGuessing and attemptNumber <= 3:
        if(userGuess.lower() == correctAnswer.lower()):
            print("Congratulations! You have entered the correct answer for this Question")
            score = score + 1
            stillGuessing = False
        else:
            attemptNumber = attemptNumber + 1
            print("Oops! You have entered the incorrect answer to this Question")
            
            if attemptNumber == 2:
                userGuess = input("Enter your second guess : ")
            if attemptNumber == 3:
                userGuess = input("Enter your third guess : ")
            if attemptNumber > 3:
                break
        
    if attemptNumber >= 3:
        print(f"Correct answer for this Question is {correctAnswer}")

score = 0
print("!!!!---- Python Programming Questions ----!!!!")
print("\nWho is the father of Python Programming Language ?")
guess_1 = input("Enter your first guess : ")
userGuessCheck(guess_1, "Guido Van Rossum")

print("\nHow many types of Operators are present in Python Programming Language ?")
guess_2 = input("Enter your first guess : ")
userGuessCheck(guess_2, "7")

print("\nWhat is the Data Type of 178.98 ?")
guess_3 = input("Enter your first guess : ")
userGuessCheck(guess_3, "Float")

print(f"\nHurray! You have completed the Python Programming Language Quiz and your score is {score}")
