def anagram(first: str, second: str) -> bool:
    """Returns True if the first and second word are anagrams.

    Note: Listen and Silent are anagrams
    """
    first_list = list(first.lower())
    second_list = list(second.lower())
    first_list.sort()
    second_list.sort()
    return first_list == second_list

first_word = input("Enter the first word: ")
second_word = input("Enter the second word: ")
if anagram(first_word, second_word):
    print(f'"{first_word}" and "{second_word}" are anagrams.')
else:
    print(f'"{first_word}" and "{second_word}" are not anagrams.')

    
print(anagram("Listen", "Silent")) 
print(anagram("hello", "world"))  
print(anagram("Debit Card", "Bad Credit"))  