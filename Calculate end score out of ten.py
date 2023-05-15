# add a point to the users final score when they answer a question correctly
# and calculate their final score out of 10

score = 0

for question, answer in questions_list[:10]:
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        score += 1

    print("Your final score is", score, "out of 10.")
