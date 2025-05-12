import sys
from stats import count_words_from_text, count_characters_from_text, sort_characters_by_count

def get_book_text(file_path):
    file_contents = None
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def display_dict_result(characters_list):
    for dict in characters_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book_to_analyze = sys.argv[1].split("/")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {"/".join(book_to_analyze[:2])}...")
    contents = get_book_text(sys.argv[1])
    num_words = count_words_from_text(contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    characters_count_list = count_characters_from_text(contents)
    characters_count_list.sort(reverse=True, key=sort_characters_by_count)
    display_dict_result(characters_count_list)
    print("============= END ===============")

main()