def who_is_missing(file_name):
    """
    Reads a file containing comma-separated integers, searches for a missing integer within the range of 1 to the
    length of the list, and writes the missing integer to a file with the same name as 'file_name'.

    Args:
        file_name (str): The name of the file to process.

    Returns:
        None

    Example:
    >> are_files_equal('test.txt')
    """
        
    with open(file_name, 'r') as read_file:
        text = read_file.read()
        integer_list = []
        for integer in text.split(','):
            integer_list.append(int(integer))

        for i in range(1, len(integer_list)+1):
            if i not in integer_list:
                with open("found.txt", 'w') as write_file:
                    write_file.write(str(i))


