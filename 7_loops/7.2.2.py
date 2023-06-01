def numbers_letters_count(input_str):
    """
    Returns a list containing the count of numbers and letters in the input string.

    Parameters:
    - input_str (str): The input string.

    Returns:
    - count_list (list): A list containing the count of numbers and letters.

    Example:
    numbers_letters_count("Hello123")
    # Output: [3, 5]
    """
    num_count = 0
    letter_count = 0

    for char in input_str:
        if char.isdigit():
            num_count += 1
        else:
            letter_count += 1

    return [num_count, letter_count]


print(numbers_letters_count("Python 3.6.3"))
