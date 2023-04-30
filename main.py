import random

# Define the questions and answers
questions = {
    "What is the Maori word for 'January'?": "Kohitātea",
    "What is the Maori word for 'February'?": "Hui-tanguru",
    "What is the Maori word for 'March'?": "Poutū-te-rangi",
    "What is the Maori word for 'April'?": "Paenga-whāwhā",
    "What is the Maori word for 'May'?": "Haratua",
    "What is the Maori word for 'June'?": "Pipiri",
    "What is the Maori word for 'July'?": "Hōngongoi",
    "What is the Maori word for 'August'?": "Here-turi-kōkā",
    "What is the Maori word for 'September'?": "Mahuru",
    "What is the Maori word for 'October'?": "Whiringa-ā-nuku",
    "What is the Maori word for 'November'?": "Whiringa-ā-rangi",
    "What is the Maori word for 'December'?": "Hakihea",
    "What is the Maori word for 'one'?": "tahi",
    "What is the Maori word for 'two'?": "rua",
    "What is the Maori word for 'three'?": "toru",
    "What is the Maori word for 'four'?": "whā",
    "What is the Maori word for 'five'?": "rima",
    "What is the Maori word for 'six'?": "ono",
    "What is the Maori word for 'seven'?": "whitu",
    "What is the Maori word for 'eight'?": "waru",
    "What is the Maori word for 'nine'?": "iwa",
    "What is the Maori word for 'ten'?": "tekau"
}

# Shuffle the questions
questions_list = list(questions.items())
random.shuffle(questions_list)

# Initialize score
score = 0

# Ask each question and check the answer
for question, answer in questions_list[:10]:
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The answer is", answer)

# Print the final score
print("Your final score is", score, "out of 10.")

