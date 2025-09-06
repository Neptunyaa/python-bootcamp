items = ["rice", "noodles", "toyo", "spam", "coffee"]
item_to_find = "spam"

for item in items:
    # TODO: If item equals the item_to_find, print and exit loop
    find = input("Enter Item: ")
    if find == item_to_find:
        print("Item found")
        break    
