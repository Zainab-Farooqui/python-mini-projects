import random

while True:
    user = input("Enter your choice rock, paper or scissors (r/p/s) :  ")
    if user not in ['r', 'p', 's']:
        print("Invalid choice, please try again.")
        break
    comp = random.choice(['r', 'p', 's']) 
    print(f"You chose: {user}")
    print(f"Computer chose: {comp}")

    if user == comp:
        print("It's a tie!")
    elif user == 'r' and comp == 's' or user == 'p' and comp == 'r' or user == 's' and comp == 'p':
        print("You win!")
    else:
        print("You lose!")
    if input("Do you want to continue? (y/n): ").lower() == 'n':
        break

