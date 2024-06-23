import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("===================================")

    while True:
        try:
            X = int(input("Enter the lower bound of the range (integer X): "))
            Y = int(input("Enter the upper bound of the range (integer Y): "))
            if X >= Y:
                print("Upper bound Y must be greater than lower bound X. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter integers only.")

    secret_number = random.randint(X, Y)
    print(f"I have selected a number between {X} and {Y}. Let's see if you can guess it!")

    attempts = 0
    guessed = False

    # Game loop
    while not guessed:
        try:

            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {secret_number} correctly.")
                print(f"It took you {attempts} attempts to guess the number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("Thank you for playing!")

number_guessing_game()
