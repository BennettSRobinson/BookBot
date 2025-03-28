def get_book_text_word_length(text):
    words = text.split()
    return len(words)

def get_duplicate_characters(text):
    dict = {}
    for char in text:
        curr_char = char.lower()
        if curr_char in dict:
            dict[curr_char] += 1
        else:
            dict[curr_char] = 1
    return dict

def sort_dups(dict):
    sorted_dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    return sorted_dict