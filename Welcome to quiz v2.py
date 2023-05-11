# Welcome the user to the quiz then give them a choice to either continue with the quiz
# or to exit the quiz
# V2 adding instructions

print("Welcome to this Māori language quiz!")
user_input = input("Press Enter to proceed or type 'no' to quit: ")
if user_input.lower() == "no":
    print("Thank you for considering this quiz. Goodbye!")
else:
    print("Let's get started with the quiz!")

    print("You will be given 10 questions which you will answer. At the end you will then be given a score out of 10. "
          "Remember to write the numbers as e.g. one instead of 1")
