def update_playlist(file_path, new_song):
    """
    Update an MP4 playlist file with a new song.

    If the playlist has less than two songs, the new song will be added as the second song.
    Otherwise, the song in the third line of the playlist will be replaced with the new song.

    Args:
        file_path (str): The path of the playlist file.
        new_song (str): The new song to be added or used as a replacement.
    """
    with open(file_path) as file:
        lines = file.readlines()

    line_change = 0 if len(lines) < 2 else 2
    song_parts = lines[line_change].split(';')
    song_parts[0] = new_song
    lines[line_change] = ';'.join(song_parts)

    if line_change < 2:
        updated_content = '\n' + '\n' + lines[line_change]
    else:
        updated_content = ''.join(lines)

    with open(file_path, 'w') as file:
        file.write(updated_content)


update_playlist('songs.txt', 'Python Love Story')
