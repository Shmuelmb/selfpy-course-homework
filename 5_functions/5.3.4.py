def last_early(my_str):
    """
    Checks if the last character in the given string is present earlier in the string.

    Args:
        my_str (str): The input string to check.

    Returns:
        bool: True if the last character is present earlier in the string, False otherwise.
    """
    my_str = my_str.lower()  # Convert the string to lowercase for case-insensitive comparison.
    last_char = my_str[-1]  # Get the last character of the string.

    # Check if the last character is present earlier in the string (excluding the last character itself).
    return last_char in my_str[:-1]


print(last_early("example"))  # Output: True
print(last_early("hello"))  # Output: False

