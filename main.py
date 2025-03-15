import sys
from stats import *

def get_book_text(fpath):
    with open(fpath, "r") as f:
        return f.read()


def print_report(num_words, num_chars_sorted, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in num_chars_sorted:
        if not entry['char'].isalpha():
            continue
        print(f"{entry['char']}: {entry['count']}")
    print("============= END ===============")

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = f"{sys.argv[1]}"
    file_contents = get_book_text(path)
    num_words = get_word_count(file_contents)
    num_chars = get_char_count(file_contents)
    num_chars_sorted = build_sorted_list(num_chars)
    print_report(num_words, num_chars_sorted, path)

if __name__ == "__main__":
    main()