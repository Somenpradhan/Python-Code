import random

def number_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it correctly.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 10

    for attempt in range(1, attempts + 1):
        try:
            # Ask the user to input their guess
            guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly in {attempt} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    else:
        print(f"Sorry, you've used all {attempts} attempts. The number was {secret_number}.")

# Run the game
if __name__ == "__main__":
    number_game()
