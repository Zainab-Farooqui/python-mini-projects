import random
guess = random.randint(1, 100)
while True:
    user = int(input("Guess a number between 1 and 100: "))
    if user> guess:
        print("Too high! Try again.")
    elif user < guess:
        print("Too low! Try again.")
    else:
        print("Congratulations! You've guessed the number correctly.")
        break