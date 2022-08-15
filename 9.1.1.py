def are_files_equal(file1, file2):
    x = open(file1, 'r')
    y = open(file2 , 'r')
    if x.read() == y.read():
        return (True)
    else:
        return (False)
