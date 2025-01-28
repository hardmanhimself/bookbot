def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report on {book_path} ---")
    print(f"{num_words} words found in document")
    print()
    for item in chars_sorted_list:
        if item["letter"].isalpha():
            print(f"The '{item["letter"]}' character was found {item["num"]} times")
    print("--- End report ---")
    
    
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


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
