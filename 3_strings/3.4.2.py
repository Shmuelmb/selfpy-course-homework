# Prompting the user to enter a string
x = input("Please enter a string:\n")

# Modifying the string by replacing 'd' with 'e' starting from the second character
modified_string = "d" + x[1::].replace('d', 'e')

# Printing the modified string
print(modified_string)
