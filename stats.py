def get_num_words(text):
    words = text.split()
    return len(words)

def chars_dict_to_sorted_list(chars_dict):
    chars_dict_list = []
    for c in chars_dict:
        chars_dict_list.append({"letter": c, "num": chars_dict[c]})
    chars_dict_list.sort(reverse=True, key=sort_on)
    return chars_dict_list


def sort_on(dict):
    return dict["num"]


def get_chars_dict(text):
    lowered_text = text.lower()
    char_count = {}
    for letter in set(lowered_text):
        char_count[letter] = lowered_text.count(letter)
    return char_count