def check_win(secret_word, old_letters_guessed):
    """
    Checks if the player has won the game by guessing all the letters in the secret word.

    Parameters:
    - secret_word (str): The secret word that the player needs to guess.
    - old_letters_guessed (list): A list of letters that the player has guessed so far.

    Returns:
    - is_won (bool): True if the player has won, False otherwise.

    Example:
    secret_word = "shmuel"
    old_letters_guessed = ["a", "m", "p", "s", "h", "u", "e", "l", "l"]
    print(check_win(secret_word, old_letters_guessed))
    # Output: True
    """

    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False

    return True


secret_word = "shmuel"
old_letters_guessed = ["a", "m", "p", "s", "h", "u", "e", "l", "l"]
print(check_win(secret_word, old_letters_guessed))
