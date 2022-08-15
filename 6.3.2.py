def longest(my_list):
    my_list.sort(key=len)
    return (my_list[-1])

    

list1 = ["111", "234", "2000", "goru", "birthday", "09"]
print(longest(list1))
