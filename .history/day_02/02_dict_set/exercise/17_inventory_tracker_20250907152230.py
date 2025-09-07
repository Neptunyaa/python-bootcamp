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
    """TODO: Print the items and their details line-by-line"""
    print("Inventory:")



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
            add(inventory, item)

        elif command == "remove":
            #  TODO: Use remove command"""
            name = input("Item name: ")
            info = input("Item info: ")
            item = {"Name": name, "Info": info}
            remove(inventory, item)
        elif command == "read":
            # TODO: Use read command"""
            name = input("Item name: ")
            info = input("Item info: ")
            item = {"Name": name, "Info": info}
            read(inventory, item)
        elif command == "show":
            # TODO: Use show command"""
            name = input("Item name: ")
            info = input("Item info: ")
            item = {"Name": name, "Info": info}
            print(inventory, item)
        elif command == "exit":
            running = False
        else:
            print(" Use add, remove, read, show, or exit.")    


main()
