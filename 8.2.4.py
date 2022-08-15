def sort_anagrams(list_of_strings):
    a = []
    for word in list_of_strings:
        b = []
        for i in list_of_strings:
            if sorted(word) == sorted(i):
                b.append(i)
        if b not in a:
            a.append(b)
                
               


    return a
       
       
    
        
list_of_words = ['apple', 'dog', 'aba', 'god', 'aplpe']
print(sort_anagrams(list_of_words))



