def last_early(my_str):
    my_str = my_str.lower()
    z = my_str[-1]
    
    if z in my_str[0:-1]:
      return True  
    else: 
       return False
    
 


