import random
from termcolor import cprint

QUESTION = "question"
OPTIONS = "options"
ANSWER = "answer"


def ask_question(index, question, options):
    print(f"Question {index + 1}. {question}")
    for option in options:
        print(option)

    return input("Your answer: ").upper().strip()


def run_quiz(quiz):
    random.shuffle(quiz)

    score = 0
    for index, item in enumerate(quiz):
        answer = ask_question(
            index, item[QUESTION], item[OPTIONS])

        if answer == item[ANSWER]:
            cprint("Correct!", "green")
            score += 1
        else:
            cprint(f"Wrong! The correct answer is {item[ANSWER]}", "red")

        print()

    print(f"Quiz over! Your final score is {score} out of {len(quiz)}.")


def main():
    quiz = [
        {
            QUESTION: "What is the capital of France?",
            OPTIONS: ["A. Paris", "B. London", "C. Rome", "D. Madrid"],
            ANSWER: "A"
        },
        {
            QUESTION: "Which is the largest planet in our solor system?",
            OPTIONS: ["A. Earth", "B. Jupiter", "C. Mars", "D. Mercury"],
            ANSWER: "B"
        },
        {
            QUESTION: "What is the largest ocean on earth?",
            OPTIONS: ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
            ANSWER: "D"
        }
    ]
    run_quiz(quiz)


if __name__ == "__main__":
    main()
