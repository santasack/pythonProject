import random

print("Welcome to this Māori language quiz!")
user_input = input("Press Enter to proceed or type 'no' to quit: ")
if user_input.lower() == "no":
    print("Thank you for considering this quiz. Goodbye!")
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

    # Define the questions and answers
    qa_pairs = [
        ("January", "What is the English word for 'Kohitātea'?"),
        ("February", "What is the English word for 'Hui-tanguru'?"),
        ("March", "What is the English word for 'Poutū-te-rangi'?"),
        ("April", "What is the English word for 'Paenga-whāwhā'?"),
        ("May", "What is the English word for 'Haratua'?"),
        ("June", "What is the English word for 'Pipiri'?"),
        ("July", "What is the English word for 'Hōngongoi'?"),
        ("August", "What is the English word for 'Here-turi-kōkā'?"),
        ("September", "What is the English word for 'Mahuru'?"),
        ("October", "What is the English word for 'Whiringa-ā-nuku'?"),
        ("November", "What is the English word for 'Whiringa-ā-rangi'?"),
        ("December", "What is the English word for 'Hakihea'?"),
        ("one", "What is the English word for 'tahi'?"),
        ("two", "What is the English word for 'rua'?"),
        ("three", "What is the English word for '#toru'?"),
        ("four", "What is the English word for 'whā'?"),
        ("five", "What is the English word for 'rima'?"),
        ("six", "What is the English word for 'ono'?"),
        ("seven", "What is the English word for 'whitu'?"),
        ("eight", "What is the English word for 'waru'?"),
        ("nine", "What is the English word for 'iwa'?"),
        ("ten", "What is the English word for 'tekau    '?")
    ]

    # Shuffle the questions
    random.shuffle(qa_pairs)

    # Show score
    score = 0

    # Ask each question and check the answer
    for answer, question in qa_pairs[:10]:
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print(formatter("!", "CORRECT"))
            print()
            score += 1
        else:
            print("Incorrect. The answer is", answer)

    # Show the final score
    print("Your final score is", score, "out of 10.")
