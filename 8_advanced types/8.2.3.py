def generate_combinations(tuple1, tuple2):
    """
    Generates combinations of elements from two tuples.

    Parameters:
    tuple1 (tuple): The first tuple.
    tuple2 (tuple): The second tuple.

    Returns:
    tuple: A tuple containing combinations of elements from tuple1 and tuple2.
    """
    combinations = []

    for item1 in tuple1:
        for item2 in tuple2:
            combinations.extend(((item1, item2), (item2, item1)))
    return tuple(combinations)


first_tuple = (1, 2)
second_tuple = (4, 5)
print(generate_combinations(first_tuple, second_tuple))
