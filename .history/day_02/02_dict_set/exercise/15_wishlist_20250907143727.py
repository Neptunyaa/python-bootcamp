# TODO: Fill in the details of the item you plan to buy
order = {
    "Name": "Jerson",
    "Info": "Yummiest guy of Cavite",
}

# TODO: Print the item details in the following format:
"""
Order:
	Name: item name
	Info: item info
	...
"""
print("Order:")
for key, value in order.items():
	print(f"\t{key}: {value}")
