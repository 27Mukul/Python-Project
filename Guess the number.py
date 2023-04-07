import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Initialize the number of guesses to 0
num_guesses = 0

# Start the game loop
while True:
    # Ask the user to guess the number
    guess = int(input("Guess the number (between 1 and 100): "))
    
    # Increment the number of guesses
    num_guesses += 1
    
    # Check if the guess is correct
    if guess == number:
        print(f"Congratulations! You guessed the number in {num_guesses} tries!")
        break
    elif guess < number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")