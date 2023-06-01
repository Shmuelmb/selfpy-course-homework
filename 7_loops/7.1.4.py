
def squared_numbers(start, stop):
    """
    Returns a list of squared numbers between the given start and stop values (inclusive).

    Parameters:
    - start (int): The starting number.
    - stop (int): The ending number.

    Returns:
    - squared (list): A list containing the squared numbers.

    Example:
    squared_numbers(4, 8)  # Output: [16, 25, 36, 49, 64]
    squared_numbers(-3, 3)  # Output: [9, 4, 1, 0, 1, 4, 9]
    """
    squared = []
    num = start
    while num <= stop:
        squared.append(num * num)
        num += 1
    return squared

        
print(squared_numbers(-3, 3))




