from random import randint

random_number = randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number (between 1 and 100): "))

        if guess > random_number:
            print("Too high!")
        elif guess < random_number:
            print("Too low!")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Invalid guess! Enter a valid number.")
