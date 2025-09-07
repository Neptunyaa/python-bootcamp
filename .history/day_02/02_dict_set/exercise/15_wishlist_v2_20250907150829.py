# TODO: Fill in the details of the items you plan to buy
order = {
    "Name": "Jerson",
    "Info": "Yummiest guy of Cavite",
	"Age": "25",
	"Hobby": "Eating",
},
{
	"Name": "Alice",
	"Info": "Adventurous",
	"Age": "30",
	},

# TODO: Print the item details in the following format (for each order):
"""
Order:
	Name: item name
	Info: item info
	...
"""
for key, value in order.items():
	print(f"\t{key}: {value}")