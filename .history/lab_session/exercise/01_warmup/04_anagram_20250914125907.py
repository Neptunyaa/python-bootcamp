def anagram(first: str, second: str) -> bool:
    """Returns True if the first and second word are anagrams.

    Note: Listen and Silent are anagrams
    """

def anagram(first: str, second: str) -> bool:
    """Returns True if the first and second word are anagrams.

    Note: Listen and Silent are anagrams
    """
    first_list = list(first.lower())
    second_list = list(second.lower())
    first_list.sort()
    second_list.sort()
    return first_list == second_list

print(anagram("Listen", "Silent")) 
print(anagram("hello", "world"))  
print(anagram("Debit Card", "Bad Credit"))  