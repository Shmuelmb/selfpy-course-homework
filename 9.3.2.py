def my_mp4_playlist(file_path, new_song): 
    file = open(file_path, 'r')
    text_words = file.read()
   
    l = list(text_words)
    for i in range(len(l)):
        if l[i] == ';':
            s.append(i)
          
    s[5] = s[5] + 1

    new_song = '\n' + new_song
        
    x = text_words.replace(text[s[5]:s[6]], new_song)

    file.close()

    file_2 = open(file_path, 'w')
    file_2.write(x)
    print(x)
    file_2.close()

my_mp4_playlist('C:/Users/shmuel/Desktop/songs.txt', 'ho')
