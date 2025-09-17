import sys
from stats import count_words, count_chars, format_dict

def get_book_text(f):
    with open(f) as file:
        return file.read()

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]

    book_string = get_book_text(path)
    book_word_count = count_words(book_string)
    book_char_count = count_chars(book_string)
    formatted_chars = format_dict(book_char_count)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {book_word_count} total words
--------- Character Count -------""")
    for element in formatted_chars:
        print(f"{element['char']}: {element['num']}")
    print("============= END ===============")

main()
