# Number Guessing Game

### Goal

Write a program to have the computer randomly select a number between 1 and 100, and then prompt the player to guess the number. The program should give hints if the guess is too high or too low.

### Solution

1. Generate a number between 1 and 100 and store it a variable called random_number.
2. Ask user to guess the number.
3. If the guess is higher than the random number, print "Too high"
4. If the guess is lower than the random number, print "Too low"
5. If the guess is the same as the random number, congratulate the user and stop the program.
6. To keep the program running until the user guess the number, wrap the codes in a while loop.
7. To prevent user from entering an invalid guess such as a character, we wrap the code in a try-except block to handle the ValueError Exception, and ask the user to enter a valid number if there's an invalid input.

Note: The if-else statement needs to be inside the try block because the guess variable was set inside the block.
