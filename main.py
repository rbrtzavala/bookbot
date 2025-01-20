def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_numb_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = get_chars_sorted_list(chars_dict)
    chars_sorted_list = sorted(chars_list, reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for entry in chars_sorted_list:
            print(f"The '{entry["letter"]}' character was found '{entry["count"]}' times")

    print("--- End report ---")
    
def get_numb_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_chars_dict(text):
    char_dictionary = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_dictionary:
            char_dictionary[lowered_char] += 1
        else:
            char_dictionary[lowered_char] = 1     
    return char_dictionary

def get_chars_sorted_list(dict):
    chars_list = []
    for key, value in dict.items():
        if key.isalpha():
            chars_list.append({"letter": key, "count": value})     
    return chars_list

def sort_on(dict):
    return dict["count"]

main()