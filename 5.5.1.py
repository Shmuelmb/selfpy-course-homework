import string
def is_valid_input(letter_guessed):
	
    if len(letter_guessed) > 1:
        return False
    elif  letter_guessed in string.punctuation: 
        return False
    elif letter_guessed in string.digits:
        return False
    else:
         return True
			
print(is_valid_input("1"))
print(is_valid_input("!"))
print(is_valid_input("a1"))
print(is_valid_input("a"))
