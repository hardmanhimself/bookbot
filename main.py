from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
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


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
