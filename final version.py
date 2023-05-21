# Final version

import random

print("Welcome to this Māori language quiz!")
user_input = input("Press Enter to proceed or type 'no' to quit: ")
if user_input.lower() == "no":
    print("Thank you for considering this quiz. Have a nice day!")
else:
    print("Let's get started with the quiz!")

    def formatter(symbol, text):
        sides = symbol * 3
        formatted_text = f"{sides} {text} {sides}"
        top_bottom = symbol * len(formatted_text)
        return f"{top_bottom}\n{formatted_text}\n{top_bottom}"

    print(formatter("*", "Welcome to this Māori language quiz! You will be asked 10 questions and given"
                         " a score out of 10."))
    print()

    print("You will be given 10 questions which you will answer. At the end you will then be given a score out of 10. "
          "Remember to write the numbers as e.g. one instead of 1")

    # questions and answers
    questions = {
        "What is the English word for 'Kohitātea'?": "January",
        "What is the English word for 'Hui-tanguru'?": "February",
        "What is the English word for 'Poutū-te-rangi'?": "March",
        "What is the English word for 'Paenga-whāwhā'?": "April",
        "What is the English word for 'Haratua'?": "May",
        "What is the English word for 'Pipiri'?": "June",
        "What is the English word for 'Hōngongoi'?": "July",
        "What is the English word for 'Here-turi-kōkā'?": "August",
        "What is the English word for 'Mahuru'?": "September",
        "What is the English word for 'Whiringa-ā-nuku'?": "October",
        "What is the English word for 'Whiringa-ā-rangi'?": "November",
        "What is the English word for 'Hakihea'?": "December",
        "What is the English word for 'tahi'?": "one",
        "What is the English word for 'rua'?": "two",
        "What is the English word for 'toru'?": "three",
        "What is the English word for 'whā'?": "four",
        "What is the English word for 'rima'?": "five",
        "What is the English word for 'ono": "six",
        "What is the English word for 'whitu'?": "seven",
        "What is the English word for 'waru'?": "eight",
        "What is the English word for 'iwa'?": "nine",
        "What is the English word for 'tekau'?": "ten"
    }

    # Shuffle the questions
    questions_list = list(questions.items())
    random.shuffle(questions_list)

    # Show score
    score = 0

    # Ask each question and check the answer
    for question, answer in questions_list[:10]:
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print(formatter("!", "CORRECT"))
            print()
            score += 1
        else:
            print("Incorrect. The answer is", answer)

    # Show the final score
    print("Your final score is", score, "out of 10.")
    if score < 3:
        print("You suck learn some Maori!")
    elif score <= 5 >= 3:
        print("Eh you've got some learning to do")
    elif score <= 8 > 5:
        print("Well done mate your quite good at this")
    elif score >= 9:
        print("Your a Maori language genius!")  
