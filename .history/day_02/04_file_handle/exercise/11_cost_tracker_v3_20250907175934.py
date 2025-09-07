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
    if expenses:
        print("Expenses:", expenses)
        print("Total:", sum(expenses))
    else:
        print("No expenses recorded.")


def save(expenses):
    """TODO: Save the current list of expenses to a new file"""
    with open("cost_tracker.txt", 'w') as file:
        for expense in expenses:
            file.write(f"Spends: {expense}\n")
    print(f"Expenses saved to cost_tracker.txt")


def load(expenses):
    """Load expenses from a file and update the expenses list"""
    try:
        with open("cost_tracker.txt", 'r') as file:
            expenses.clear()
            for line in file:
                if line.startswith("Spends:"):
                    amount = line.strip().split(":")[1].strip()
                    expenses.append(int(amount))
        print("Expenses loaded from cost_tracker.txt")


def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(current_expenses)
        elif command == "refund":
            refund(current_expenses)
        elif command == "show":
            show(current_expenses)
        elif command == "save":
            save(current_expenses)
        elif command == "load":
            load(current_expenses)        
        elif command == "quit":
            running = False
        else:
            print(" Use spend, refund, show, save, load or quit.")


main()
