
def squared_numbers(start, stop):           # this func take 2 numbers(start allways < stop), and return all the squared beetwen us
    squared = []
    while start < stop or start == stop:
        squared.append(start*start)         # example: if start = 4, and stop = 8, the func return 4*4 and 5*5 and 6*6 and 7*7 and 8*8
        start+=1
    return squared
        
        
        
print(squared_numbers(-3, 3))




