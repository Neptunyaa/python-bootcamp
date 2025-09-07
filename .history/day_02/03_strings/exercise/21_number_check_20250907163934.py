# Ask the user for an input
user_input = input("Enter number: ").strip()

# TODO: If user enters a valid number
if user_input.isnumeric():
    user_input = int(user_input)
    print(user_input + 1)

# TODO: Else
else:
    print("Please enter a valid number!")
    print(user_input)
