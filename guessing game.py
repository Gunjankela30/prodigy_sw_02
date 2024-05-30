import random

def main():
    print("Welcome to the Number Guessing Game!")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    # Loop until the user guesses the number correctly
    while not guessed_correctly:
        try:
            # Prompt the user for a guess
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            # Compare the guess to the generated number
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
                print(f"It took you {attempts} attempts to guess the number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
