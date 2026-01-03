def count_words(bookText):
    words = bookText.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_characters(bookText):
    character_dict = {}
    for char in bookText:
        if char.lower() not in character_dict:
            character_dict[char.lower()] = 1
        else:
            character_dict[char.lower()] += 1
    return character_dict