def are_files_equal(file1, file2):
    """
    Compare the content of two files and check if they are equal.

    Args:
        file1 (str): Path to the first file.
        file2 (str): Path to the second file.

    Returns:
        bool: True if the files have the same content, False otherwise.

    Example:
        >> are_files_equal('test.txt', 'test1.txt')
        True

    """

    # Open file 1
    f1 = open(file1, 'r')
    file1_content = f1.read()

    # Open file 2
    f2 = open(file2, 'r')
    file2_content = f2.read()

    # Compare content
    are_equal = file1_content == file2_content

    # Close files
    f1.close()
    f2.close()

    return are_equal


print(are_files_equal('test.txt', 'test1.txt'))
