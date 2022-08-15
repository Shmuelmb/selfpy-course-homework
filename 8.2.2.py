def myfen(x):
   return x[1]

def sort_prices(list_of_tuples):
   return(sorted(list_of_tuples, key=myfen, reverse=True))


