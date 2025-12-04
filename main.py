from stats import get_word_count,get_character_count,get_sorted_char_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
    return ""

def main():
    book_filepath = "books/frankenstein.txt"
    book_text = get_book_text(book_filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
    
    sorted_chars = get_sorted_char_dictionary(get_character_count(book_text))
    for entry in sorted_chars:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")

main()