prod1 = int(input("Enter Number 1: "))
prod2 = int(input("Enter Number 2: "))
prod3 = int(input("Enter Number 3: "))

def product(prod1, prod2, prod3):
    products = prod1 * prod2 * prod3
    return products
    
output = product(prod1, prod2, prod3)
print(output)

# TODO: product(1, 1, 1)	# 1
# TODO: product(1, 2, 3)	# 6
# TODO: product(2, 5, 10)	# 100
# TODO: product(3, 3)	    # 9
# TODO: product(2, 5)	    # 12
