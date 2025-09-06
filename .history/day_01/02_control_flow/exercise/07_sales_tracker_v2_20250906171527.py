# TODO: Ask the user how many items will be calculated
input_count = int(input("Enter count: "))
total = 0

# TODO: Use a for loop to ask for more than one cost and count



for _ in range(1, input_count + 1):
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    item_total = item_cost * item_count
    total += item_total
print(total)
