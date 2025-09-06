"""
    TODO: Create a function `line_generator` that has a parameter `number` and prints the following:
	Line 1
	Line 2
	...
	Line number
"""

# TODO: Use the function once
number = int(input("Enter number"))
def line_generator(number):
    for number in range(number):
        print(f"Line {number}")
line_generator(number)        