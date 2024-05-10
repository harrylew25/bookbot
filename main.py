
def main() -> None:
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_counts = get_word_count(text)
    dict = get_character_count(text)
    
    generate_text_dict_report(book_path, word_counts, dict)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    lowered_case_text = text.lower()
    character_dict = {}
    for text in lowered_case_text:
        if text.isalpha() == False:
            continue
        
        if text in character_dict:
            character_dict[text] += 1
        else:
            character_dict[text] = 1
    
    return character_dict

def generate_text_dict_report(book_path, word_count, book_word_dict):
    alpha_list = sort_dict_by_count(book_word_dict)
    print(f'--- Begin report of {book_path} ---')
    print(f'{word_count} words found in the document \n')

    for item in alpha_list:
        print(f"The '{item['character']}' character was found {item['count']} times")

    print('--- End report ---')

def sort_by_count(dict):
    return dict['count']

def sort_dict_by_count(dict):
    list = []
    for character, count in dict.items():
        list.append({'character': character, 'count': count})
    list.sort(reverse=True,key=sort_by_count)
    return list

main()