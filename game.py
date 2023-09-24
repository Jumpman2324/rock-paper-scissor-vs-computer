import random

while True:
    user_choice = input("rock (r) paper (p) or scissors (s): ")

    computer_choice = random.choice(["r", "p", "s"])

    def determine_winner():
        if user_choice == computer_choice:
            print("its a draw")
        elif user_choice == 'r' and computer_choice == 's' or user_choice == 'p' and computer_choice == 'r' or user_choice == 's'and computer_choice == 'p':
            print("you won")
        else:
            print("computer won")


    determine_winner()