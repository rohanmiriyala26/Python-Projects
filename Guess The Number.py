import random
def generate_number():
    return random.randint(1, 100)
def start():
    number = generate_number()
    guess = None
    num_guesses = 0
    print("Welcome to the guessing game!")
    while guess != number:
        guess = int(input("Guess the number between 1 and 100: "))
        num_guesses += 1
        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
    print(f"Congratulations! You guessed the number in {num_guesses} tries.")
start()
