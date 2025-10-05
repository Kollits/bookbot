def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def main():
    file_contents = get_book_text()
    print(file_contents)

main()