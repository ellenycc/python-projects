from random import sample

while True:
    answer = input("Roll the dice? (y/n): ").strip().lower()
    if answer == "y":
        """generate two random numbers between 1 and 6"""
        print(tuple(sample(range(1, 7), k=2)))
    elif answer == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
