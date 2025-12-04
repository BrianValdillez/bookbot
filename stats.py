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

def sort_on(char_entry):
    return char_entry["num"]

def get_sorted_char_dictionary(dictionary):
    sorted_dictionary = []
    for c in dictionary:
        sorted_dictionary.append({"char": c, "num": dictionary[c]})

    sorted_dictionary.sort(key=sort_on, reverse=True)
    return sorted_dictionary