def extend_list_x(list_x, list_y):
     list_y[5:] = list_x[:3]
     return list_y
    

x = [4, 5, 6]
y = [1, 2, 3]

print(extend_list_x(x,y))
