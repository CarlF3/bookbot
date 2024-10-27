def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text)

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

def print_report(text: str):
    words = count_words(text)
    chars = count_characters(text)
    chars_list = []
    for char in chars:
        if char.isalpha():
            chars_list.append({"char": char, "count": chars[char]})
    chars_list.sort(reverse=True, key=lambda dict: dict["count"] )


    print("--- Start of Report ---")
    print(f"The text contains {words} words.\n")
    for i in range(0, len(chars_list)):
        print(f"The character \"{chars_list[i]['char']}\" apears {chars_list[i]['count']} times.")
    print("--- End of Report ---")

main()