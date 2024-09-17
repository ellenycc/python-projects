# Rock Paper Scissor Game

### Goal

Write a program to simulate a game of Rock, Paper, Scissors. The game will prompt the player to choose rock, paper, or scissors by typing 'r', 'p', or 's'. The computer will randomly select its choice. The game will then display both choices using emojis and determine the winner based on the rules.

### Solution

1. Prompt the user to choose between 'r', 'p', or 's' using the `input()` function. By using a tuple to store the choices, we can ensure they won't be accidentally edited.

   ```python
       choices = ("r", "p", "s")

       user_choice = input("Rock, paper or scissors? (r/p/s): ").lower()
   ```

2. Check for any invalid input. If the user's choice is not in the choices tuple, print "Invalid choice".

   ```python
       if user_choice not in choices:
           print("Invalid choice!")
   ```

3. Generate the computer choice. First, we need to import the random module. Then, we can use the `choice()` function on the choices tuple to randomly select a choice for the computer. We can store this choice in a variable called computer_choice.

   ```python
       computer_choice = random.choice(choices)
   ```

4. Print the user and computer choices. To display the emojis instead of the letters, create a dictionary with key-value pairs mapping the letters to the corresponding emojis. Then, access the emoji value by using the user_choice as the key.

   ```python
       emojies = {"r": "🪨", "p": "📄", "s": "✂️"}

       print(f"You chose {emojies[user_choice]}")
       print(f"Computer chose {emojies[computer_choice]}")
   ```

5. Based on different scenarios, we print the result of the game.

   ```python
       if user_choice == computer_choice:
           print("Tie")
       elif (
           (user_choice == "r" and computer_choice == "s") or
           (user_choice == "p" and computer_choice == "r") or
           (user_choice == "s" and computer_choice == "p")):
           print("You win!")
       else:
           print("You lose")
   ```

6. To allow the user to continue playing, we can use a while loop. After getting the result, we prompt the user if they want to continue. If the answer is "no", the game stops. If the answer is "yes", the game is played again.

   ```python
       while True:
           user_choice = input("Rock, paper or scissors? (r/p/s): ").lower()
           # Code for playing the game

           continue_game = input("Contine? (y/n): ").lower()
           if continue_game == "n":
               break
   ```

This while loop ensures that the game keeps running until the user decides to stop playing.

### Refactoring

7. To improve code modularity and maintainability, we extract segments of code into functions with a single responsibility. This allows for easier understanding, testing, and reusability of the code.

   ```python
       def get_user_choice():
           while True:
               user_choice = input("Rock, paper or scissors? (r/p/s): ").lower()
               if user_choice in choices:
                   return user_choice
               else:
                   print("Invalid choice!")


       def display_choices(user_choice, computer_choice):
           print(f"You chose {emojies[user_choice]}")
           print(f"Computer chose {emojies[computer_choice]}")


       def determine_winner(user_choice, computer_choice):
           if user_choice == computer_choice:
               print("Tie")
           elif (
               (user_choice == ROCK and computer_choice == SCISSORS) or
               (user_choice == PAPER and computer_choice == ROCK) or
                   (user_choice == SCISSORS and computer_choice == PAPER)):
               print("You win!")
           else:
               print("You lose")
   ```

   We can call the `get_user_choice()`, `display_choices()`, and `determine_winner()` functions inside the `play_game()` function. Finally, we call `play_game()` at the end to run the program.

   ```python
       def play_game():
           while True:
               user_choice = get_user_choice()

               computer_choice = random.choice(choices)

               display_choices(user_choice, computer_choice)

               determine_winner(user_choice, computer_choice)

               continue_game = input("Contine? (y/n): ").lower()
               if continue_game == "n":
                   break

       play_game()
   ```

8. Apply the DRY (Don't Repeat Yourself) principle by defining the choices in a single place. This way, we can easily make changes to the choices without having to update them in multiple locations.

   ```python
     ROCK = "r"
     SCISSORS = "s"
     PAPER = "p"
     emojies = {ROCK: "🪨", PAPER: "📄", SCISSORS: "✂️"}
     choices = tuple(emojies.keys())
   ```

   By defining the choices as constants and using them consistently throughout the code, we can avoid crashing the program due to typos and make it easier to update the choices in the future.

   ```python
       def determine_winner(user_choice, computer_choice):
           if user_choice == computer_choice:
               print("Tie")
           elif (
               (user_choice == ROCK and computer_choice == SCISSORS) or
               (user_choice == PAPER and computer_choice == ROCK) or
                   (user_choice == SCISSORS and computer_choice == PAPER)):
               print("You win!")
           else:
               print("You lose")
   ```
