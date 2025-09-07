# Ask the user for an input
email_input = input("Enter your email address: ")

# TODO: If valid gmail address
for email in [email_input]:
    if email_input.endswith("@gmail.com"):
        print("This is a valid gmail address")
    break

# TODO: Else
else:
    print("This is NOT a valid gmail address")
