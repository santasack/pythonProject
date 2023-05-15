# Right/Wrong checker v2
# Same as v1 but I add the questions for testing
import random

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

questions_list = list(questions.items())
random.shuffle(questions_list)



for question, answer in questions_list[:10]:
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")



        else:
            print("Incorrect. The answer is", answer)
