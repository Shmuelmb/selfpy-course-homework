def who_is_missing(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        
    l = []
    l = list(text.split(','))
    l = list(map(int, l))
    l = (sorted(l))


    s = []

    for i in (l):
        s.append(int(i) + 1)
        
    x = 0
    if len(l) > 1:
        for y in s:
            if y not in l and y < l[-1]:
                return(y)
                x = y
    else:
        return l[-1] - 1
        
