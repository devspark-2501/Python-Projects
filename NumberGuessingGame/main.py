import random

print('-----------------------------------------------')
number = random.randint(1, 100)
attempts = 0

print('Welcome to the Number Guessing Game!')
print('I have selected a number between 1 and 100. Can you guess it?')
print('-----------------------------------------------')

while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.")

    else:
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        break
