user_input = input("Guess a letter: ").lower()
if len(user_input) > 1:
    if user_input.isalpha():
        print("E1")
    else:
        print("E3")
else:
    if user_input.isalpha():
        print(user_input)
    else:
        print("E2")
