import string


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Check if a letter input is valid based on the following criteria:
    1. The letter should be a single character.
    2. The letter should not be a punctuation mark.
    3. The letter should not be a digit.
    4. The letter should not have been guessed before.

    Args:
        letter_guessed (str): The letter input to be checked.
        old_letters_guessed (list): A list of previously guessed letters.

    Returns:
        bool: True if the letter is valid, False otherwise.
    """

    if len(letter_guessed) != 1:
        return False
    if letter_guessed in string.punctuation or letter_guessed in string.digits:
        return False
    return letter_guessed.lower() not in old_letters_guessed


# Example usage
guessed_letters = ['a', 'b', 'c']
print(check_valid_input('D', guessed_letters))  # Output: True
print(check_valid_input('a', guessed_letters))  # Output: False
