def my_mp3_playlist(file_path):
    file = open(file_path)
    text = file.read()

    l = list(text)
    list_of_line = []   
    k = ''.join(l[::])
    list_of_line = list(k.split("\n"))
    list_of_true = []
    songs = []

    for i in list_of_line:
        songs.append(i.split(';'))
        
    len_of_songs  = (len(songs)) # כמות השירים בקובץ


    time = []
    for x in songs:
        for strings in (x[2:3]):
            y = int(strings.replace(":", ""))
            time.append(y)
            sorted(time)
            if time[0] == int(strings.replace(":", "")):
                list_of_true = (x[0:1]) # השיר הכי ארוך

    list_of_true.append(len_of_songs)

    artists = []
    for artist in songs:
        for p in artist[1:2]:
            artists.append(p)
    o = []
    for i in artists:
        x = (artists.count(i))
        t = [x,i]
        if t not in o:
            o.append(t)
    o.sort()

    list_of_true.append(o[-1][1]) #האומן שמופיע הכי הרבה פעמים
    return(tuple(list_of_true))
