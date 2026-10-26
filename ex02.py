import random

user = input("Choose R, P, or S: ")
computer = random.choice(("R", "P", "S"))

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")

elif user == "R" and computer == "S":
    print("You win!")

elif user == "P" and computer == "R":
    print("You win!")

elif user == "S" and computer == "P":
    print("You win!")

else:
    print("Computer wins!")