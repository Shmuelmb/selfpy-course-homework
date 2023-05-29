import string


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    if (
            len(letter_guessed) > 1
            or letter_guessed in string.punctuation
            or letter_guessed in string.digits
            or letter_guessed in old_letters_guessed
    ):
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True

    # example:


old_letter = ["b", "a", "c"]
print(try_update_letter_guessed("a", old_letter))
