
def count_words(book_string):
    """Takes string from get_book_text as its input and counts the number of words."""
    word_list = book_string.split()
    total_words = len(word_list)
    return total_words

def count_characters(book_string):
    """Takes a string from get_book_text as its input and counts how many times each
    character occurs."""
    search_text = book_string.lower()
    character_count ={}
    for char in search_text:
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] += 1
    return character_count

def sort_on(listed_count):
    return listed_count["chars"]

def sort_count(character_count):
    """Sorts a character frequency dictionary as a list of dicts for pretty 
    printing."""
    list_of_chars = []
    for key in character_count:
        new_dict = {"char": key, "chars": character_count[key]}
        list_of_chars.append(new_dict)
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars
