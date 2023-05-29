def shift_left(my_list):
    """
    Shifts the elements in a list to the left by one position.

    Args:
        my_list (list or str): The input list to be shifted.

    Returns:
        list: A new list with elements shifted to the left.

    Example:
        >> shift_left("123")
        ['2', '3', '1']
    """
    my_list = list(my_list)  # Convert the input to a list
    a, b, c = my_list  # Unpack the first three elements of the list
    return [b, c, a]  # Return a new list with elements shifted to the left


print(shift_left("123"))

