def add(total):
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    total = item_cost * item_count
    return total 


def sub(total):
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    total_item_cost = item_cost * item_count
    return total - total_item_cost


def show(total):
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    total_item_cost = item_cost * item_count
    print(total_item_cost)


def main():
    total = 0
    running = True
    while running:
        command = input("Provide command: ")
        if command == "command 1":
            total = add(total)
        elif command == "command 2":
            total = sub(total)
        elif command == "command 3":
            total = show(total)          
        elif command == "exit":
            running = False


main()
