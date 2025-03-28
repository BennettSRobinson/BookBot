from stats import get_book_text_word_length
from stats import get_duplicate_characters
from stats import sort_dups
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_name = sys.argv[1]
        file_text = get_book_text(file_name)
        num_words = get_book_text_word_length(file_text)
        duplicate_characters = get_duplicate_characters(file_text)
        sorted_duplicate_characters = sort_dups(duplicate_characters)
        print("===================== BookBot ==========================")
        print(f"Analyzing book found at {file_name}")
        print("--------------------- Word Count -----------------------")
        print(f"Found {num_words} total words")
        print("---------------------- Character Count -----------------")
        for key, value in sorted_duplicate_characters:
            print(f"{key}: {value}")

main()