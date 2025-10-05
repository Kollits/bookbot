import sys
from stats import get_num_words
from stats import get_num_characters


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

BOOK_PATH = sys.argv[1]

def get_book_text():
    with open(BOOK_PATH) as f:
        return f.read()

def main():
    file_contents = get_book_text()
    count = get_num_words(file_contents)
    char_counts = get_num_characters(file_contents)
    sorted_char_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char, num in sorted_char_counts:
        print(f"{char}: {num}")
    print("============= END ===============")
main()