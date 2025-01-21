import random


def guess_number():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100

    # Generate a random number
    random_number = random.randint(lower_bound, upper_bound)

    print(f"Welcome to the Number Guessing Game!")
    print(f"Guess the number between {lower_bound} and {upper_bound}.")

    attempts = 0
    while True:
        try:
            # User input for guessing the number
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct, too high, or too low
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {random_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")


# Run the game
if __name__ == "__main__":
    guess_number()
