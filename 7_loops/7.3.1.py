def show_hidden_word(secret_word, old_letters_guessed):
    em_list = [s_s for s_s in secret_word if s_s not in old_letters_guessed]
    true_c = ''.join(em_list)
    for x in secret_word:
        if x in true_c: # in - זה ההבדל בין הדרך הזו לדרך השניה 
            secret_word = (secret_word.replace(x,"_"))
    return " ".join(secret_word)
      
   
secret_word = "shmuel"
old_letters_guessed = ["a","m","p","s"]
print(show_hidden_word(secret_word, old_letters_guessed))
