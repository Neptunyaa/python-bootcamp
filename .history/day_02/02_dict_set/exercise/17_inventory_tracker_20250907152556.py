def add(inventory, item):
    """TODO: Add a new item (dict) to the inventory (list[dict])"""
    inventory.append(item)


def remove(inventory, index):
    """TODO: Remove item (dict) in the given index (int) of inventory"""
    inventory.pop(index)


def read(inventory, index):
    """TODO: Return the item (dict) in the given index (int) of inventory"""
    return inventory[index]


def show(inventory):
    """Print the items and their details line-by-line"""
    print("Inventory:")
    for index, item in enumerate(inventory):
        print(f"{index}: {item}")



def main():
    running = True
    inventory = []

    while running:
        command = input("Command: ")
        if command == "add":
            # TODO: Use add command"""
            name = input("Item name: ")
            info = input("Item info: ")
            item = {"Name": name, "Info": info}
        elif command == "remove":
            #  Use remove command
            try:
                index = int(input("Index to remove: "))
                remove(inventory, index)
            except (ValueError, IndexError):
                print("Invalid index.")
        elif command == "read":
            # Use read command
            try:
                index = int(input("Index to read: "))
                item = read(inventory, index)
                print(item)
            except (ValueError, IndexError):
                print("Invalid index.")
        elif command == "show":
            # Use show command
            show(inventory)
            # TODO: Use show command"""
            print(inventory, item)
        elif command == "exit":
            running = False
        else:
            print(" Use add, remove, read, show, or exit.")    


main()
