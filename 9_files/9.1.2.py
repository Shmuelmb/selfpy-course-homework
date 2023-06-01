def process_text_file(file_path):
    """
    Reads a text file, performs various operations based on user input, and prints the results.

    Args:
        file_path (str): The path to the text file.

    Returns:
        None
    """
    file = open(file_path, 'r')
    text = file.read()
    file.close()

    task = input('Enter a task ("sort", "rev", or "last"): ')

    characters = list(text)
    line_indices = [i for i, char in enumerate(characters) if char == '\n']

    if task == 'sort':
        words = text.split()
        unique_words = list(set(words))
        sorted_words = sorted(unique_words)
        print(sorted_words)
    elif task == 'rev':
        reversed_lines = text[::-1].split("\n")
        for line in reversed_lines:
            print(line)
    elif task == 'last':
        num_lines = int(input('Enter the number of lines to retrieve from the end: '))
        last_lines = ''.join(characters[line_indices[-num_lines]:])
        print(last_lines)
    else:
        print('Invalid task. Please enter either "sort", "rev", or "last".')


file_path = input('enter a file patch: ')

process_text_file(file_path)
