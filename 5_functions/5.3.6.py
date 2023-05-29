def fix_age(age):
    """
    Fixes the given age if it falls within specific ranges.

    Parameters:
    - age (int): The age to be fixed.

    Returns:
    - int: The fixed age, which is 0 if the age is between 16 and 19 (exclusive) or between 11 and 15 (exclusive), otherwise the original age.
    """

    return 0 if 19 > age > 16 or 11 < age < 15 else age


def filter_teens(a=13, b=13, c=13):
    """
    Filters the given ages based on the fix_age function and returns the sum of the fixed ages.

    Parameters:
    - a (int): The first age.
    - b (int): The second age.
    - c (int): The third age.

    Returns:
    - int: The sum of the fixed ages.
    """

    return fix_age(a) + fix_age(b) + fix_age(c)

    
