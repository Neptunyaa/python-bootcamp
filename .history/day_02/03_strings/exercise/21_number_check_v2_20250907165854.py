# Ask the user for an input
user_input = input("Enter number: ").strip()

if user_input.isdigit():
    user_input = int(user_input)
    print(user_input + 1)
else:
    print("Please enter a valid number!")
