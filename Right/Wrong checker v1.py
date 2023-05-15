# Checks if users answer is right or wrong

if user_answer.lower() == answer.lower():
    print(formatter("!", "CORRECT"))
    print()
    score += 1
else:
    print("Incorrect. The answer is", answer)
