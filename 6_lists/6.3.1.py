def are_lists_equal(list1, list2):
    """
    Checks if two lists are equal regardless of the order of their elements.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        bool: True if the lists are equal, False otherwise.

    Example:
        >> list1 = [0.6, 1, 2, 3]
        >> list2 = [3, 2, 0.6, 1]
        >> list3 = [9, 0, 5, 10.5]
        >> print(are_lists_equal(list1, list2))
        True
        >> print(are_lists_equal(list1, list3))
        False
    """
    return sorted(list1) == sorted(list2)


list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]

print(are_lists_equal(list1, list2))
print(are_lists_equal(list1, list3))
