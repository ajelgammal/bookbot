# main.py
from pathlib import Path
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    rel_path = "books/frankenstein.txt"  # printed in the report exactly like this
    base = Path(__file__).resolve().parent
    text = get_book_text(base / rel_path)

    num_words = get_num_words(text)
    char_counts = get_char_counts(text)
    sorted_chars = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {rel_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():            # skip non-alphabetical chars
            print(f"{ch}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

