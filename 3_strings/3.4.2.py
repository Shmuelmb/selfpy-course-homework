# Prompting the user to enter a string
input_user = input("Please enter a string:\n")

# Modifying the string by replacing 'd' with 'e' starting from the second character
modified_string = "d" + input_user[1::].replace('d', 'e')

# Printing the modified string
print(modified_string)
