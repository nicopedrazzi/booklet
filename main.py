from stats import get_text, get_book_text, get_letter_number, sort_dict, tot_let
import sys

def main():
    if len(sys.argv)==2:
        path=sys.argv[1]
        text = get_book_text(path)
        words, x = get_text(text)
        dict = get_letter_number(words)
        sorted = sort_dict(dict)

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {x} total words")
        print("--------- Character Count -------")
        for item in sorted:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()

