def seven_boom(end_number):
    """
    Generates a list of numbers and "BOOM" based on the given end_number.
    
    The function iterates from 0 to end_number (inclusive) and checks each number. If the number contains the digit 7
    or is divisible by 7, it replaces the number with the string "BOOM" in the generated list.

    Parameters:
    - end_number (int): The maximum number until which the list is generated.
    
    Returns:
    - boom_list (list): A list of numbers and "BOOM" based on the given end_number.
    
    Example: seven_boom(57) # Output: [0, 1, 2, 3, 4, 5, 6, "BOOM", 8, 9, 10, 11, 12, 13, "BOOM", 15, 16, "BOOM", 18,
    19, 20, 21, "BOOM", 23, 24, 25, 26, "BOOM", 28, 29, "BOOM", "BOOM", "BOOM", "BOOM", "BOOM", "BOOM", "BOOM",
    "BOOM", "BOOM", "BOOM", "BOOM", "BOOM", "BOOM", "BOOM", "BOOM", "BOOM", "BOOM", "BOOM", "BOOM", "BOOM", "BOOM",
    "BOOM", "BOOM", "BOOM", 50, 51, 52, "BOOM", 54, 55, 56, "BOOM"]
    """
    boom_list = []
    for num in range(end_number + 1):
        if "7" in str(num) or num % 7 == 0:
            boom_list.append("BOOM")
        else:
            boom_list.append(num)
    return boom_list


print(seven_boom(57))
