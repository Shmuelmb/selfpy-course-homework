import string
def check_valid_input(letter_guessed, old_letters_guessed):
    old_letters_guessed = list(old_letters_guessed)
    if len(letter_guessed) > 1:
        return False
    elif  letter_guessed in string.punctuation: 
        return False
    elif letter_guessed in string.digits:
        return False
    elif letter_guessed.lower() in old_letters_guessed:
        return False
    else:
         return True
			



