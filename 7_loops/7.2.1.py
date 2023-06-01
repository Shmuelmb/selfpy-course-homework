def is_greater(numbers, threshold):
    """
    Returns a new list containing numbers greater than the given threshold.

    Parameters:
    - numbers (list): A list of numbers.
    - threshold (int): The threshold value.

    Returns:
    - greater_numbers (list): A list of numbers greater than the threshold.

    Example:
    is_greater([1, 30, 25, 60, 27, 28], 28)
    # Output: [30, 60, 27]
    """
    
    greater_numbers = []
    for num in numbers:
        if num > threshold:
            greater_numbers.append(num)
    return greater_numbers

