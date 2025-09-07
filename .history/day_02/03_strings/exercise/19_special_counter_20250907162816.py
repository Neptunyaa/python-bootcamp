string = input('Enter string: ')
special_count = 0
special_char = '!@#$%^&*()'

# TODO: Add one to special_count for each special char in string
for special_count in special_char:
    if string in special_char:
        special_count += 1
print(f"Special Character {special_count}")
