def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = count_words(file_contents)
    chars_dict = list_all_chars(file_contents)
    list_of_dicts = convert_dic_to_list_of_dicts(chars_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    print_report(book_path, file_contents, word_count, list_of_dicts)

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def list_all_chars(text):
    result = {}
    for char in text.lower():
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def convert_dic_to_list_of_dicts(chars_dict):
    allChars = list(chars_dict)
    result = []
    for char in allChars:
        if char.isalpha():
            single_char_dict = {}
            single_char_dict["name"] = char
            single_char_dict["num"] = chars_dict[char]
            print(single_char_dict)
            result.append(single_char_dict)
    return result

def sort_on(dict):
    return dict["num"]


def print_report(path, text, word_count, chars_dict_list):
    name= "name"
    num = "num"
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for dict in chars_dict_list:
        print(f"The '{dict[name]}' character was found {dict[num]} times")
    print("--- End report ---")
main()