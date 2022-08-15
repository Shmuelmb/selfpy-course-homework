def my_mp4_playlist(file_path, new_song): 
    file = open(file_path, 'r')
    text = file.readlines()
    
    list_of_strings= []
    for i in text:
        list_of_strings.append(i.split(';'))
    l = [""]
    if len(list_of_strings) > 2:
        list_of_strings.append(l)
        new_song = new_song 
        list_of_strings[2][0] = new_song
        
    while len(list_of_strings) == 2:
        list_of_strings.append(l)
        new_song = new_song + ';'
        list_of_strings[2][0] = new_song
        
    while len(list_of_strings) < 2:
        list_of_strings.append(l)
        new_song ='\n'+ new_song + ';'
        list_of_strings[1][0] = new_song
    
    ll = []
    for i in list_of_strings:
        ll.append(";".join(i))

    
        
    x = "".join(ll)
    print(x)
        
        
        


my_mp4_playlist('C:/Users/shmuel/Desktop/songs.txt', 'ho')
