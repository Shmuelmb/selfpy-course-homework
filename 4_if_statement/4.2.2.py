# check if string is palindrome
user_input = input("Enter a string: ").replace(" ", "").lower()

# If this string is the same string if it is reversed
# for example -> wow is palindrome and palindrome is not palindrome :)
if user_input == user_input[::-1]:
    print("This string is palindrome")
else:
    print("This string not palindrome")
