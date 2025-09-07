def spend(expenses):
    """TODO: Add a new cost in expenses"""
    try:
        amount = int(input("Enter amount spent: "))
        expenses.append(amount)
        print(f"Added expense: {amount}")
    except ValueError:
        print("Invalid amount. Please enter a number.")


def refund(expenses):
    """TODO: Remove the last cost added (if any)"""
    if expenses:
        removed = expenses.pop()
        print(f"Refunded last expense: {removed}")
    else:
        print("No expenses to refund.")


def show(expenses):
    """TODO: Print the current list of expenses and total"""


def save(expenses):
    """TODO: Save the current list of expenses to a new file"""


def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(current_expenses)


main()
