import random
import string
def generate_password(length, complexity):
    if complexity == "low":
        chars = string.ascii_lowercase
    elif complexity == "medium":
        chars = string.ascii_letters + string.digits
    elif complexity == "high":
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Choose 'low', 'medium', or 'high'.")
    password = ''.join(random.choice(chars) for i in range(length))
    return password
def create():
    length = int(input("Enter the length of the password: "))
    complexity = input("Enter the complexity of the password (low/medium/high): ").strip().lower()
    try:
        password = generate_password(length, complexity)
        print("Your password is:", password)
    except ValueError as e:
        print(e)
create()
