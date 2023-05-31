
input_user = input("Please enter a string: ")
result = input_user[:len(input_user)//2].lower() + input_user[len(input_user)//2:].upper()
print(result)
