from stats import *

def get_book_text(fpath):
    with open(fpath, "r") as f:
        return f.read()


def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    num_words = get_word_count(file_contents)
    num_chars = get_char_count(file_contents)
    print(f"{num_words} words found in the document")
    print(num_chars)
    

if __name__ == "__main__":
    main()