# Basic code for the decoration of my quiz


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"

print(formatter("!", "CORRECT"))
print()

print(formatter("*", "Welcome to this Māori language quiz! You will be asked 10 questions and given"
                     " a score out of 10."))
print()