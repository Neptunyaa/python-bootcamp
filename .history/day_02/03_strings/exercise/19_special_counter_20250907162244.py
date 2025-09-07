string = input('Enter string: ')
special_count = 0
special_char = '!@#$%^&*()'

# TODO: Add one to special_count for each special char in string
special_count += 1
for special_count in special_char:
    if special_char in string:
        special_count += 1
print(special_count)
