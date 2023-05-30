import string


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Tries to update the guessed letter in the list of old guessed letters.
    
    Args:
        letter_guessed (str): The letter guessed by the player.
        old_letters_guessed (list): The list of previously guessed letters.
    
    Returns:
        bool: True if the letter is successfully updated in the list, False otherwise.
    """
    letter_guessed = letter_guessed.lower()

    if (
            len(letter_guessed) > 1
            or letter_guessed in string.punctuation
            or letter_guessed.isdigit()
            or letter_guessed in old_letters_guessed
    ):
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False

    old_letters_guessed.append(letter_guessed)
    return True


# Example usage:
old_letters = ["b", "a", "c"]
print(try_update_letter_guessed("a", old_letters))
