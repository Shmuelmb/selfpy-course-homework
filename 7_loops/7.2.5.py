def sequence_del(my_str):
    """
    Removes consecutive duplicate characters from the input string.

    The function iterates over the characters of the input string and keeps track of the previously seen character.
    If the current character is different from the previous character, it is added to the result string.

    Parameters:
    - my_str (str): The input string to process.

    Returns:
    - result (str): The processed string with consecutive duplicate characters removed.

    Example:
    my_str = "aaabbbccc"
    sequence_del(my_str)
    # Output: "abc"

    my_str = "hello"
    sequence_del(my_str)
    # Output: "helo"
    """
    prev = ""
    for letter in my_str:
        if letter not in prev:
            prev += letter
    return prev


my_str = "aaabbbccc"
print(sequence_del(my_str))
