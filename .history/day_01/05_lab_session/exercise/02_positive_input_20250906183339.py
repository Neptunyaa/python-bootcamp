# TODO: Ask the user for an input that should be a number
number = int(input("Enter number: "))

# TODO: Then try to convert this into an integer using the following:
number_converted = int(number)

# The user could provide an invalid integer input (string)
# TODO: Handle this case
def number():
    while True:
        numbers = input("Enter a numbers: ") 
        try:
            number = int(number)
        except:
            print("Negative number, try again")
            continue

            if numbers < 0:
                print("Negative number, try again")
            continue  
            break
print("Correct number")                 


# The user could give a negative number
# TODO: Handle this case

# Challenge: TODO: Give the user infinite times to retry


