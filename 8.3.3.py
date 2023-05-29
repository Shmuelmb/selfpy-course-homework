def count_chars(my_str):
    return {i: my_str.count(i) for i in list(my_str)}

my_str = 'aabbbcccc'
print(count_chars(my_str))
