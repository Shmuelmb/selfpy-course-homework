def count_chars(my_str):
    d = {}
    my_str = my_str.replace(" ","")
    for i in my_str:
        if i not in d:
            d[i] = my_str.count(i)
        
    return d
my_str = 'aabbbcccc'
print(count_chars(my_str))
