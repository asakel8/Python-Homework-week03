import random

user_score = 0
computer_score = 0

play = "yes"

while play == "yes":

    user = input("Choose R, P, or S: ")
    computer = random.choice(("R", "P", "S"))

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif user == "R" and computer == "S":
        print("You win!")
        user_score = user_score + 1

    elif user == "P" and computer == "R":
        print("You win!")
        user_score = user_score + 1

    elif user == "S" and computer == "P":
        print("You win!")
        user_score = user_score + 1

    elif user in ["R", "P", "S"]:
        print("Computer wins!")
        computer_score = computer_score + 1

    print("Your score:", user_score)
    print("Computer score:", computer_score)

    play = input("Do you want to play again? (yes/no): ")

print("Thanks for playing!")