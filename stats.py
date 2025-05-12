
def count_words_from_text(text):
    text_as_list = text.split()
    return len(text_as_list)

def count_characters_from_text(text):
    list_with_characters = []
    count_characters_dict = {}
    for character in text.lower():
        if character in count_characters_dict:
            count_characters_dict[character] += 1
        else:
            count_characters_dict[character] = 1
    for key in count_characters_dict:
        list_with_characters.append(
            { "char": key, "num": count_characters_dict[key] }
        )
    return list_with_characters

def sort_characters_by_count(character_count):
    return character_count["num"]