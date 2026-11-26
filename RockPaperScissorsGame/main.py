
import random

Choices = ['rock', 'paper', 'scissors']
computer_score = 0
player_score = 0

print('-----------------------------------------------')
print('       🎮 Welcome to Rock Paper Scissors!      ')
print('-----------------------------------------------')

while True:
    player = input('Enter your choice (rock, paper, scissors) or type (Q) to quit: ').lower()

    if player == "q":
        break

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
        player_score += 1

    else:
        print("😢 Computer wins!")
        computer_score += 1

    print('-----------------------------------------------')
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    print('-----------------------------------------------')

print("\nThanks for playing!")

print('-----------------------------------------------')
print(f"Final Player Score: {player_score}")
print(f"Final Computer Score: {computer_score}")
print('-----------------------------------------------')
