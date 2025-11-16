"""
This function for counting words in a book
"""


def count_book_words(text):
    return f"Found {len(text.split())} total words."


"""
Creates dictionary of character count in books
"""


def get_book_chars(text):
    book = {}
    for i in text:
        i = i.lower()
        if i in book:
            book[i] += 1
        else:
            book[i] = 1
    return book


def sort_on(items):
    return items["num"]


def sort_dicts(d):
    list = []
    for i in d:
        list.append({"name": i, "num": d[i]})
    list.sort(reverse=True, key=sort_on)

    return list


def get_book_sorted_chars(text):
    return sort_dicts(get_book_chars(text))
