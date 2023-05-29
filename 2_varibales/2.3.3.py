# Prompting the user to enter three numbers
print("Enter 3 numbers to check the remainder of their sum when divided by 3")
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

# Calculating the sum of the three numbers
sum_numbers = num_1 + num_2 + num_3

# Performing division to check the remainder
division_without_remainder = sum_numbers // 3
division_includes_remainder = (sum_numbers / 3) - division_without_remainder
remainder_whole_number = sum_numbers % 3

# Printing the results
print(f'the sum of numbers is  {sum_numbers}')
print(f'the divided numbers without remainder is  {division_without_remainder}')
print(f'the divided numbers includes remainder is  {division_includes_remainder}')
print(f'the remainder whole number is  {remainder_whole_number}')
print(f"Is there no remainder? {division_includes_remainder == 0.0}")


