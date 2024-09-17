# Quiz Game

## Goal

Write a program to create a quiz where the player answers multiple-choice questions. The program should evaluate the player's answers and provide a score at the end.

## Key Takeaways

1. Use of Constants

   We replace string keys used repeatedly in dictionaries with constant variables. In Python, we don't really have true Constants like in Java, C++, C#, they are basically variables. But by convention, we use uppercase letters to treat them as constants. This reduces typos and makes it easier to maintain the code.

   ```python
   QUESTION = "question"
   OPTIONS = "options"
   ANSWER = "answer"
   ```

2. Useful VS code shortcuts

   Duplicate: highlight text, then press ctrl + shift + opt + down arrow
   Expand selection ctrl + cmd + shift + right arrow
   Shrink selection ctrl + cmd + shift + left arrow

3. Avoid global variables

   They can lead to bugs that are difficult to trace. Instead, variables like quiz are passed as function arguments to avoid unintended side effects.

4. Parameters vs Arguments

   A parameter is a variable defined when we create a function, like a placeholder, whereas an argument is an actual value passed into a function when we call it.

5. `random.shuffle()` is used to randomize the order of question in the quiz.

6. The `enumerate()` function is used to iterate over a sequence like a list, tuple or string while keeping track of both the index and the value at the same time.

7. Use of termcolor library's cprint() for colored output to enhance user experience

   Syntax:
   enumerate(iterable, start=0)

8. Use `print()` to create a linebreak for better user experience.
