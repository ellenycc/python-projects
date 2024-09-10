# Dice Rolling Game

### Goal

Write a program that simulates rolling a pair of dice. Each time the program runs, it should randomly generate two numbers between 1 and 6 (inclusive), representing the result of each die. The program should then display the results and ask if the user would like to roll again.

### Solution

1. Ask the user if they want to roll the dice.
2. If the user enters "y", generate two random numbers between 1 and 6 and print the numbers. Here we import sample() function from the random module to generate a tuple of two random numbers.
3. If the user enters "n", print the message "Thanks for playing!" and stop the program.
4. If the user types either "y" or "n", print "Invalid choice".
5. We want to keep prompting the user input until the user enters "n", so we wrap all the logic in a while loop.
