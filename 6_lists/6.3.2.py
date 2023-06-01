def longest(my_list):
    """
    Finds and returns the longest string from a list.

    Args:
        my_list (list): The list of strings.

    Returns:
        str: The longest string in the list.

    Example:
        >> list1 = ["111", "234", "2000", "goru", "birthday", "09"]
        >> print(longest(list1))
        birthday
    """
    return(max(my_list, key=len))


list1 = ["111", "234", "2000", "goru", "birthday", "09"]
print(longest(list1))

