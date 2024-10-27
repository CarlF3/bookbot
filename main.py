def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print(count_words(text))

def count_words(book: str):
    word_array = book.split()
    return len(word_array)

def get_book_text(path: str):
    with open(path) as book:
        return book.read()


main()