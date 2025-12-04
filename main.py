from stats import get_word_count,get_character_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
    return ""

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {get_word_count(book_text)} total words")
    print(get_character_count(book_text))
    #print(get_book_text("books/frankenstein.txt"))

main()