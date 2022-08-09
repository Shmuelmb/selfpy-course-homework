def mult_tuple(tuple1, tuple2):
    l = []
    for i in tuple1:
        for x in tuple2:
            l.append((i,x))
            l.append((x,i))
    def convert(list):
        return tuple(list)
    return convert(l)

first_tuple = (1, 2)
second_tuple = (4, 5)
print(mult_tuple(first_tuple, second_tuple))
