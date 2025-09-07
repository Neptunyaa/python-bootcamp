# Ask the user for an input
user_input = input("Enter number: ")

# TODO: Remove extra spaces
user_input = user_input.strip()
# TODO: Remove commas
user_input = user_input.replace(",", "")
# TODO: Remove extra spaces
user_input = user_input.split()
user_input = "".join(user_input)

# TODO: If user enters a valid number
if user_input.isnumeric():
    user_input = int(user_input)
    print(user_input + 1)
# TODO: Else
else:
    print("Please enter a valid number!")

