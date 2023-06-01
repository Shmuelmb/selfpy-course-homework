def inverse_dict(dictionary):
    """
    Create an inverse dictionary where keys are values and values are lists of keys.

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        dict: An inverted dictionary where keys are values from the input dictionary,
              and values are lists of keys with the same value.

    Example:
        >> inverse_dict({'b': 'd', 'a': 'd', 'c': 'd'})
        {'d': ['b', 'a', 'c']}
        >> inverse_dict({'I': 3, 'love': 3, 'self.py!': 2})
        {3: ['I', 'love'], 2: ['self.py!']}

    """
    inverse = {}
    for key, value in dictionary.items():
        if value in inverse:
            inverse[value].append(key)
        else:
            inverse[value] = [key]
    return inverse


# Example usage
print(inverse_dict({'b': 'd', 'a': 'd', 'c': 'd'}))
print(inverse_dict({'I': 3, 'love': 3, 'self.py!': 2}))
