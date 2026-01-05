def count_words(bookText):
    words = bookText.split()
    count = 0
    for word in words:
        count += 1
    return count

def get_chars_dict(bookText):
    chars = {}
    for char in bookText:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_chars_dict(chars):
    dict_list = []
    for char in chars:
        num = chars[char]
        dict_list.append({"char": char, "num": num})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list