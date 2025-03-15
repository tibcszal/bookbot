from stats import get_word_count

def get_book_text(fpath):
    with open(fpath, "r") as f:
        return f.read()


def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    num_words = get_word_count(file_contents)
    print(f"{num_words} words found in the document")
    

if __name__ == "__main__":
    main()