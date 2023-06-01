def choose_word(file_path, index):
    """
    Choose a word from a file based on the given index.

    The function reads the contents of the file, splits it into individual words, and selects a word based on the provided index.
    If the index exceeds the number of words, it wraps around using the modulo operator.

    Args:
        file_path (str): The path of the file.
        index (int): The index of the word to choose.

    Returns:
        tuple: A tuple containing the count of unique words in the file and the chosen word.

    """
    with open(file_path) as f:
        data_file = f.read().split()
        index = index % len(data_file) - 1

        word_count = len(set(data_file))

        return word_count, data_file[index]


word_count, chosen_word = choose_word('songs.txt', 3)
print("Number of unique words:", word_count)
print("Chosen word:", chosen_word)
