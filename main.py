def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print(count_characters(text))

def count_words(text: str):
    word_array = text.split()
    return len(word_array)

def get_book_text(path: str):
    with open(path) as book:
        return book.read()
    
def count_characters(text: str):
    chars = {}
    for char in text.lower():
        if char in chars.keys():
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

main()