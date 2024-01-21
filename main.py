def main():
    book_loc = "books/frankenstein.txt"
    print(f"--- Start analalysis of {book_loc} ---")
    text = read_text(book_loc)
    word_count = count_words(text)
    print(f"There are {word_count} words in the document")
    letter_count = count_letters(text)
    print_letter_count(letter_count)
    print(f"--- End analalysis ---")

def read_text(book_path: str) -> str:
    with open(book_path) as f:
        return f.read()

def count_words(book: str) -> int:
    return len(book.split())

def count_letters(book: str) -> dict:
    letter_dict = {}
    for letter in book:
        if letter.lower() in letter_dict:
            letter_dict[letter.lower()] += 1
        else:
            letter_dict[letter.lower()] = 1
    return letter_dict

def print_letter_count(letter_dict: dict) -> None:
    sorted_list = sorted(letter_dict.items(), key=lambda x: x[1], reverse= True)
    for letter, count in sorted_list:
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")

    
main()