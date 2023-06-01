def extend_list_x(list_x, list_y):
    """
    Extends list_x by appending the elements of list_y.

    Args:
        list_x (list): The list to be extended.
        list_y (list): The list containing elements to append.

    Returns:
        list: The extended list.

    Example:
        >> x = [4, 5, 6]
        >> y = [1, 2, 3]
        >> print(extend_list_x(x, y))
        [1, 2, 3, 4, 5, 6]
    """
    list_y[3:] = list_x
    return list_y


x = [4, 5, 6]
y = [1, 2, 3]

print(extend_list_x(x, y))
