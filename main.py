from stats import get_num_words, get_list_char, get_sorted_char
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
        book_text = get_book_text(path_to_book)
        num_words = get_num_words(book_text)
        list_char = get_list_char(book_text)
        sorted_char = get_sorted_char(list_char)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_book}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for c in sorted_char:
            print(f"{c["char"]}: {c["num"]}")
        
        print("============= END ===============")

main()
