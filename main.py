import sys

from stats import count_book_words, get_book_chars, get_book_sorted_chars


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def create_book_report(file_path):
    character_count = get_book_sorted_chars(get_book_text(file_path))
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book foud at {file_path}")
    print("----------- Word Count ----------")
    print(count_book_words(get_book_text(file_path)))
    print("----------- Character Count ----------")
    for i in character_count:
        if i["name"].isalpha():
            print(f"{i['name']}: {i['num']}")

    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        create_book_report(sys.argv[1])


main()
