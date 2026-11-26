import random

Choices = ['rock', 'paper', 'scissors']
# computer_score = 0
# player_score = 0

print('-----------------------------------------------')
print('       🎮 Welcome to Rock Paper Scissors!      ')
print('-----------------------------------------------')

while True:
    player = input('Enter your choice (rock, paper, scissors) or type (Q) to quit: ').lower()

    if player not in Choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(Choices)

    print('-----------------------------------------------')
    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")
    print('-----------------------------------------------')

    if player == computer:
        print("🤝 It's a draw!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("🎉 You win!")

    else:
        print("😢 Computer wins!")

    play_again = input("\nPlay again? (y/n): ").lower()

    if play_again != "y":
        print("Thanks for playing!")
        break
