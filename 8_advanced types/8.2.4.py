def sort_anagrams(list_of_strings):
    """
    Sorts a list of strings into groups of anagrams.

    Parameters:
    list_of_strings (list): A list of strings representing words without spaces.

    Returns:
    list: A list of lists, where each inner list contains words that are anagrams of each other.
    """

    # Create a dictionary to store groups of anagrams
    anagram_groups = {}

    # Iterate through each string in the input list
    for word in list_of_strings:
        # Sort the letters of the word to create a unique key for anagram groups
        sorted_word = ''.join(sorted(word))

        # Check if the sorted word exists as a key in the dictionary
        if sorted_word in anagram_groups:
            # If the key exists, append the word to the corresponding group
            anagram_groups[sorted_word].append(word)
        else:
            # If the key does not exist, create a new group with the word
            anagram_groups[sorted_word] = [word]

    return list(anagram_groups.values())


list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
print(sort_anagrams(list_of_words))
