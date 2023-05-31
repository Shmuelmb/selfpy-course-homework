import string


def is_valid_input(letter_guessed):
    """
    Checks if the given letter guessed is a valid input.

    Parameters:
    - letter_guessed (str): The letter guessed to be validated.

    Returns:
    - bool: True if the letter is a valid input, False otherwise.
    """

    return (
            len(letter_guessed) <= 2
            and letter_guessed not in string.punctuation
            and letter_guessed not in string.digits
    )


print(is_valid_input("1"))
print(is_valid_input("!"))
print(is_valid_input("a1"))
print(is_valid_input("a"))
