def get_word_count(book):
    return len(book.split())

def get_character_count(book):
    dictionary = {}

    book_lower = book.lower()
    for c in book_lower[0::]:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1
               
    return dictionary