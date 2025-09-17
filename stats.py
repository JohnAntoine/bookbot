from utils import sort_on_num

def count_words(string):
    word_array = string.split()
    return len(word_array)

def count_chars(string):
    char_count = {}
    for c in string:
        if c.lower() not in char_count:
            char_count[c.lower()] = 1
        else:
            char_count[c.lower()] += 1
    return char_count

def format_dict(dictionary):
    out = []
    for key in dictionary:
        if key.isalpha():
            out.append({"char": key, "num": dictionary[key]})
        else:
            continue
    out.sort(reverse=True, key=sort_on_num)
    return out
