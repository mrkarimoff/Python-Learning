# Rock, paper, scissor game

import sys
import random

play_again: bool | str = True

while play_again:
    player_choice = input(
        "\nEnter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n"
    )
    player = int(player_choice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computer_choice = random.choice("123")
    computer = int(computer_choice)

    print("\nYou chose " + player_choice + ".")
    print("Python chose " + computer_choice + ".\n")

    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python Wins!")

    play_again = input("\nPlay again? \nY for Yes or\nQ to Quit\n\n")

    if play_again.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        play_again = False

sys.exit("Bye! 👋")
