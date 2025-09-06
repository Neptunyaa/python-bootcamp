# TODO: Ask the user for an input that should be a number
# number = int(input("Enter number: "))

# TODO: Then try to convert this into an integer using the following:
# number_converted = int(number)

# The user could provide an invalid integer input (string)
# TODO: Handle this case
def positive_number():
    while True:
        numbers = input("Enter a numbers: ") 
        try:
            if numbers < 0:
                print("Negative number, try again")
            else:
                return numbers
        except ValueError:
            print("Invalid input, try again")
numbers = positive_number()
print("Correct number", numbers)                 


# The user could give a negative number
# TODO: Handle this case

# Challenge: TODO: Give the user infinite times to retry


