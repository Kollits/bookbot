def get_num_words(file_contents):
    count = 0
    for word in file_contents.split():
        count += 1
    return count


def get_num_characters(file_contents):
    char_counts = {}
    for char in file_contents.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts