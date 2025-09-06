# TODO: Ask the user for an input that should be a number
number = int(input("Enter number: "))

# TODO: Then try to convert this into an integer using the following:
number_converted = int(number)

# The user could provide an invalid integer input (string)
# TODO: Handle this case
while True:
    numbers = input("Enter a numbers: ") 
    try:
        number_converted = int(number)
        if numbers < 0:
            print("Negative number, Enter positive number")
        else:
            print("Positive Number!")
        break
    except ValueError:
        print("")        


# The user could give a negative number
# TODO: Handle this case

# Challenge: TODO: Give the user infinite times to retry


