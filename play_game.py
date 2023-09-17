import random
while True:
    user_choice= input("Please enter your choice (rock, paper, scissor): ").lower()

    #make computer choice
    possible_choice= ("rock","scissor","paper")
    computer_choice= random.choice(possible_choice)

    #print the choice
    print(f"Your choice is {user_choice} and computer choice is {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie")

    elif user_choice == "rock":
        if computer_choice == "scissor":
            print("You win")
        else:
            print("Computer win")
    elif user_choice == "paper":
        if computer_choice == "scissor":
            print("Computer win")
        else:
            print("You win")
    elif user_choice == "scissor":
        if computer_choice == "rock":
            print("Computer win")
        else:
            print("You win")

    play_again = input("Do you want to play again?(y/n) ").lower()
    #loop
    if play_again != "y":
        break
