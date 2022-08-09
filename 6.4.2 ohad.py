def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) == 1 and letter_guessed.isalpha() == 1 and letter_guessed not in old_letters_guessed:    #יותר מאחד לא אות ונמצא כבר בניסיונות קודמים
        old_letters_guessed += ["letter_guessed"]
        return True
    else:
        old_letters_guessed.sort()
        print("X")
        print(' -> '.join(old_letters_guessed),sep ="")
        return False
old_letter = ["b","a","c"]
print(try_update_letter_guessed("nba",old_letter))
