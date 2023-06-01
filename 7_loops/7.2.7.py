def arrow(my_char, max_length):
    """
    Generates an arrow pattern using a specified character and maximum length.

    The function constructs the arrow pattern by iteratively building each line
    of the pattern based on the current index.

    Parameters:
    - my_char (str): The character to be used for constructing the arrow pattern.
    - max_length (int): The maximum length of the arrow pattern.

    Returns:
    - pattern (str): The arrow pattern represented as a string.

    Example:
    arrow("*", 5)
    # Output:
    # *
    # **
    # ***
    # ****
    # *****
    # ****
    # ***
    # **
    # *
    """

    pattern = ""

    for i in range(1, max_length + 1):
        pattern += my_char * i + "\n"

    pattern += my_char * max_length + "\n"

    for i in range(max_length - 1, 0, -1):
        pattern += my_char * i + "\n"

    return pattern


print(arrow("*", 5))

print(arrow("*", 5))
