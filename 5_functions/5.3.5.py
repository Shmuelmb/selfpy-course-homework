def distance(a, b, c):
    """
    Check if the distance condition is satisfied.

    The function compares the values of `a`, `b`, and `c` to determine if the distance condition is satisfied.
    The condition is satisfied if:
    - `a + 1` is equal to either `b` or `c`.
    - Both `b` and `c` are greater than `a + 3`.

    Parameters:
    - a (int): First number.
    - b (int): Second number.
    - c (int): Third number.

    Returns:
    None: The function doesn't return a value. It prints the result.

    Example:
    >>> distance(1, 2, 10)
    True
    >>> distance(4, 5, 3)
    False
    """
    if a + 1 in [b, c] and (b > a + 3 or c > a + 3):
        print(True)
    else:
        print(False)

