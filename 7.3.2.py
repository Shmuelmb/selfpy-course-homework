def check_win(secret_word, old_letters_guessed):
    prev = []
    for check_secret in secret_word:
        if check_secret in old_letters_guessed:
            prev.append(check_secret)
    prev = "".join(prev)

    if len(prev) == len(secret_word):
        return True
    else:
        return False
            
          

      
      
   
secret_word = "shmuel"
old_letters_guessed = ["a","m","p","s","h","u","e","l","l"]
print(check_win(secret_word, old_letters_guessed))
