def inverse_dict(my_dict):
    new_dict  = {}
    index = 0
    dict_values = list(my_dict.values())
    dict_keys = list(my_dict.keys())
    
    for values in dict_values:
        new_dict[values] = []

    for v in dict_values:
        new_dict[v].append(dict_keys[index])
        (new_dict[v]).sort()
        index += 1

    return new_dict
    

print(inverse_dict({'b': 'd', 'a': 'd', 'c': 'd'}))
