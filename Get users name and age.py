# Get users name and age

def get_user_info():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    return name, age


user_name, user_age = get_user_info()
print("User:", user_name)
print("Age:", user_age)
