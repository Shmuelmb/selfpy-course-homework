def check_win(secret_word, old_letters_guessed):
    prev = [
        check_secret
        for check_secret in secret_word
        if check_secret in old_letters_guessed
    ]
    prev = "".join(prev)

    return len(prev) == len(secret_word)
            
          
secret_word = "shmuel"
old_letters_guessed = ["a","m","p","s","h","u","e","l","l"]
print(check_win(secret_word, old_letters_guessed))
