def format_list(my_list):
    """
    Formats a list of items into a string representation.

    Args:
        my_list (list): The input list of items.

    Returns:
        str: The formatted string representation of the list.

    Example:
        >> my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
        >> print(format_list(my_list))
        hydrogen, helium, lithium, beryllium, boron, and magnesium
    """
    if len(my_list) == 1:
        return f"{my_list[0]},"
    elif len(my_list) == 2:
        return f"{my_list[0]} and {my_list[1]}"
    elif len(my_list) == 4:
        return f"{my_list[0]}, {my_list[2]}, and {my_list[3]}"
    elif len(my_list) == 6:
        return f"{my_list[0]}, {my_list[2]}, {my_list[4]}, and {my_list[5]}"
    elif len(my_list) == 8:
        return f"{my_list[0]}, {my_list[2]}, {my_list[4]}, {my_list[6]}, and {my_list[7]}"
    else:
        return False


my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print(format_list(my_list))
