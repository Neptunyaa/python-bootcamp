# Ask the user for an input
user_input = input("Enter number: ")

# TODO: Remove extra spaces
user_input = user_input.strip()

# TODO: If user enters a valid number
if user_input.isnumeric():
    user_input = int(user_input)
    print(user_input + "|")
# TODO: Else
else:
    print("Please enter a valid number!")
