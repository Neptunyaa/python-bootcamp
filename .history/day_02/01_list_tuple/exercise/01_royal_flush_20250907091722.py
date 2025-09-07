ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Print '10','J','Q','K', and 'A' from list
royal_flush = ranks[9:] + [ranks[0]]
print(', '.join(royal_flush))
