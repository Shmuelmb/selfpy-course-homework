def sequence_del(my_str):
    prev = ""
    for letter in my_str:
        if letter not in prev:
           letter = prev + letter
           prev = letter
    return prev
        
        

        
        
            
  



my_str = "aaabbbccc"
print(sequence_del(my_str))


