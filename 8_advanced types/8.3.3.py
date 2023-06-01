def count_chars(string):
    """
    Count the occurrence of each character in a string.

    Args:
        string (str): The input string.

    Returns:
        dict: A dictionary where keys are characters and values are their counts.

    Example:
        >> count_chars('aabbbcccc')
        {'a': 2, 'b': 3, 'c': 4}
        >> count_chars('abra cadabra')
        {'a': 4, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

    """
    char_count = {}
    for char in list(string.replace(' ', '')):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# Example usage
my_str = 'aabbbcccc'
print(count_chars(my_str))
magic_str = "abra cadabra"
print(count_chars(magic_str))
