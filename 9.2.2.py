def copy_file_content(source, destination):

    with open(source, 'r') as file:
        text = file.read()
    with open(destination,'w') as file_2:
        file_2.write(text)
