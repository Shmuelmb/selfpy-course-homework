def my_mp3_playlist(filename):
    """
    Retrieves information from an MP3 playlist file.

    Args:
        filename (str): The path to the MP3 playlist file.

    Returns:
        tuple: A tuple containing:
            - longest_song (str): The name of the longest song in the playlist.
            - num_songs (int): The total number of songs in the playlist.
            - artist_with_most_songs (str): The artist with the most songs in the playlist.
    """

    lists_songs = []
    with open(filename) as file:
        songs = file.readlines()
        for song in songs:
            list_song_after_splitting = song.split(';')[:-1][::-1]
            lists_songs.append(list_song_after_splitting)

    length = len(lists_songs)
    max_time = sorted(lists_songs, reverse=True)[0][2]
    largest_number_appears = sorted(lists_songs, key=lists_songs[1].count)[-1][1]

    return length, max_time, largest_number_appears


print(my_mp3_playlist('songs.txt'))


