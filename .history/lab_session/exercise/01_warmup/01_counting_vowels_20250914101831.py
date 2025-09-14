def count_vowels(string: str) -> int:
    """Return the number of vowels in the given string"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char in vowels)

print(count_vowels())
