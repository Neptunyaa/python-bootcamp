def is_strong_password(password: str) -> bool:
    """
    Returns True if the password meets the following criteria:
    - At least 8 characters
    - Contains at least one digit
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    """
    if len(password) < 8:
        return False
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    return has_digit and has_upper and has_lower

user_password = input("Enter a password: ")
if is_strong_password(user_password):
    print("Strong password")
else:
    print("Weak password. Please ensure it meets the following criteria:")
    print("- At least 8 characters")
    print("- Contains at least one digit")
    print("- Contains at least one uppercase letter")
    print("- Contains at least one lowercase letter")
    print("- Contains at least one special character")    