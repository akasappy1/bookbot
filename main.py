import sys

from stats import count_words, count_characters, sort_count

def get_book_text(filepath):
    """Takes a filepath to a book's contents and returns them as a string."""
    with open(filepath) as f:
        book_text = f.read()
        return book_text

def main():
    try:
        book_text = get_book_text(sys.argv[1])
        frankenstein_count = count_words(book_text)
        letter_count = count_characters(book_text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {frankenstein_count} total words")
        print("--------- Character Count -------")
        final_count = sort_count(letter_count)
        for dict in final_count:
            if dict["char"].isalpha():
                print(f"{dict["char"]}: {dict["chars"]}")
        print("============= END ===============")
        sys.exit(0)
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
