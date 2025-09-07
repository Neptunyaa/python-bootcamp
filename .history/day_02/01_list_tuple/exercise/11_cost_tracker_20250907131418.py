def spend(expenses):
    """Add a new cost in expenses"""
    try:
        amount = int(input("Enter amount spent: "))
        expenses.append(amount)
        print(f"Added expense: {amount}")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def refund(expenses):
    """Remove the last cost added (if any)"""
    if expenses:
        removed = expenses.pop()
        print(f"Refunded last expense: {removed}")
    else:
        print("No expenses to refund.")

def show(expenses):
    """Print the current list of expenses and total"""
    if expenses:
        print("Expenses:", expenses)
        print("Total:", sum(expenses))
    else:
        print("No expenses recorded.")

def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ").strip().lower()
        if command == "spend":
            spend(current_expenses)
        elif command == "refund":
            refund(current_expenses)
        elif command == "show":
            show(current_expenses)
        elif command == "quit":
            running = False
        else:
            print("Unknown command. Use spend, refund, show, or quit.")

if __name__ == "__main__":
    main()
