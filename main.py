def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    report = get_report(book_path)
    
    
def get_report(book):
    text = get_book_text(book)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_dict_list = []
    for c in chars_dict:
        if c.isalpha() == True:
            mini_dict = {"letter": c, "num": chars_dict[c]}
            chars_dict_list.append(mini_dict)
    chars_dict_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report on {book} ---")
    print(f"{num_words} words found in document")
    for c in chars_dict_list:
        print(f"The '{c["letter"]}' character was found {c["num"]} times")
    print("--- End report ---")


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
