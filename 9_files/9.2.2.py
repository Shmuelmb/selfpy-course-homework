def copy_file_content(source, destination):
    """
    Copies the content of the source file to the destination file.

    Args:
        source (str): The path to the source file.
        destination (str): The path to the destination file.

    Returns:
        None
    """

    with open(source, 'r') as source_file:
        text = source_file.read()

    with open(destination, 'w') as destination_file:
        destination_file.write(text)

    print(f"Content copied from '{source}' to '{destination}' successfully.")


# Example usage:
source_file_path = 'source.txt'
destination_file_path = 'destination.txt'
copy_file_content(source_file_path, destination_file_path)
