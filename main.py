from stats import count_words, get_chars_dict, sort_chars_dict
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def display(filepath, num_words, dicts):
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {filepath}...')
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for i in range(len(dicts)):
        if dicts[i]["char"].isalpha():
            print(f'{dicts[i]["char"]}: {dicts[i]["num"]}')
    print("============= END ===============")

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

    try:
        book = get_book_text(filepath)
        num_words = count_words(book)
        chars_dict = get_chars_dict(book)
        sorted_dicts = sort_chars_dict(chars_dict)

        display(filepath, num_words, sorted_dicts)
    except Exception as e:
        print(f'Error encountered: {e}')

main()