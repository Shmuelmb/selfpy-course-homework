def inverse_dict(my_dict):
    dict_values = list(my_dict.values())
    dict_keys = list(my_dict.keys())

    new_dict = {values: [] for values in dict_values}
    for index, v in enumerate(dict_values):
        new_dict[v].append(dict_keys[index])
        (new_dict[v]).sort()
    return new_dict
    

print(inverse_dict({'b': 'd', 'a': 'd', 'c': 'd'}))
      # my_str = my_str.replace(" ","")
    # my_str = my_str.replace(" ","")
                    