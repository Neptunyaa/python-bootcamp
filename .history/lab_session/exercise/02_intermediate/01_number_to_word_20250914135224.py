def number_to_words(n: int) -> str:
    """
    Converts an integer into its English word representation.
    Example: 42 → "forty-two"

    Note: Only handle from 0 to 999,999
    """
    if n < 0 or n > 999_999:
        raise ValueError("Number out of supported range (0-999,999)")

    ones = [
        "zero", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]

    def words_under_1000(num):
        if num < 20:
            return ones[num]
        elif num < 100:
            if num % 10 == 0:
                return tens[num // 10]
            else:
                return tens[num // 10] + "-" + ones[num % 10]
        else:
            rem = num % 100
            if rem == 0:
                return ones[num // 100] + " hundred"
            else:
                return ones[num // 100] + " hundred and " + words_under_1000(rem)

    if n < 1000:
        return words_under_1000(n)
    else:
        thousands = n // 1000
        rem = n % 1000
        if rem == 0:
            return words_under_1000(thousands) + " thousand"
        else:
            if rem < 100:
                return words_under_1000(thousands) + " thousand and " + words_under_1000(rem)
            else:
                return words_under_1000(thousands) + " thousand " + words_under_1000(rem)

n = int(input("Jerson favourite number (0-999,999): "))
print(number_to_words(n))
