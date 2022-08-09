def choose_word(file_path, index):
    file = open(file_path, 'r')
    text = file.read()
    words = text.split(' ')
    
        
    
    l =[]
    for i in words:
        if i not in l:
            l.append(i)
    len_words_notin = len(l)
    
    if len(words) == 1:
        out = len_words_notin, ((words[0]))
        
    elif index > len(words):
        out = len_words_notin, ((words[index -1 - len(words)]))
    
    else:
        out = len_words_notin, ((words[index-1]))
    return(out)
