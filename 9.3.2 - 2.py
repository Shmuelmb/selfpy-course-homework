def my_mp4_playlist(file_path, new_song):
    file = open(file_path, 'r')
    l = (file.readlines())
    
    if len(l) == 1:
        new_song ='\n'+ ',\n' + new_song+ ';'
        l.append(new_song)
    print(l) 
    
    
    
    text = ''.join(l)
    print(text)
    file.close()
    file_2 = open(file_path, 'w')
    file_2.write(text)
    file_2.close()
my_mp4_playlist('C:/Users/shmuel/Desktop/songs.txt', 's')
