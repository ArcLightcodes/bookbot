def count_words(text):
    return len(text.split())

def get_num(dictionary):
    return dictionary["num"]


def count_characters(text):
    lowered_text = text.lower()

    # Create dictionary
    character_dictionary = {}

    for char in lowered_text:
        if char in character_dictionary:
            character_dictionary[char] += 1     # increment count if char exists
        else:
            character_dictionary[char] = 1      # initialize count if char is new
    
    return character_dictionary


def dict_to_list(dict, dict_key = "char", dict_value = "num"):
    new_list = []

    for key, value in dict.items():
        temp_dict = {dict_key: key, dict_value: value}
        new_list.append(temp_dict)      # add it to the list

    return new_list


def print_report(char_dict, filename, text):
    
    only_alphabet_char_dict = {}

    print(f"--- Begin report of {filename} ---")
    print(f"{count_words(text)} words found in the document\n")




    # only keep characters that are part of the alphabet
    for key, value in char_dict.items():
        if key.isalpha():
            only_alphabet_char_dict[key] = value
        else:
            continue    


    sorted_list = dict_to_list(only_alphabet_char_dict)
    sorted_list.sort(reverse = True, key = get_num)

    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    
    print("--- End report ---")



##########################################################################

def main():
    book_path = "books/frankenstein.txt" 
    with open(book_path) as f:
        file_contents = f.read()

        print_report(count_characters(file_contents), book_path, file_contents)


main()