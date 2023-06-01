def show_hidden_word(secret_word, old_letters_guessed):
    """
    Generates a string with the hidden word, where unguessed letters are replaced by underscores.

    Parameters:
    - secret_word (str): The secret word to be guessed.
    - old_letters_guessed (list): A list of letters guessed by the player.

    Returns:
    - hidden_word (str): The hidden word with underscores for unguessed letters.

    Example:
    secret_word = "shmuel"
    old_letters_guessed = ["a", "m", "p", "s"]
    print(show_hidden_word(secret_word, old_letters_guessed))
    # Output: "_hmu__"
    """

    hidden_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter
        else:
            hidden_word += "_"

    return hidden_word


secret_word = "shmuel"
old_letters_guessed = ["a", "m", "p", "s"]
print(show_hidden_word(secret_word, old_letters_guessed))
