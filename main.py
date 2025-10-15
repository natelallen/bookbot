def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content


def main():
    book = get_book_text("./books/frankenstein.txt")
    print(book)

main()
