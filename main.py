def main():
    with open("books/frankenstein.txt", "r") as book:
        print(count_words(book.read()))
        book.close()

def count_words(book: str):
    word_array = book.split()
    return len(word_array)


main()