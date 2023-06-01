
def get_price(item):
    """
    Helper function to extract the price from a tuple.
    
    Parameters:
    item (tuple): A tuple representing an item with its price.
    
    Returns:
    float: The price of the item.
    """
    return item[1]


def sort_prices(items):
    """
    Sorts a list of tuples based on the price in descending order.
    
    Parameters:
    items (list): A list of tuples where each tuple contains an item and its price.
    
    Returns:
    list: A sorted list of tuples in descending order based on the price.
    """
    return sorted(items, key=get_price, reverse=True)

