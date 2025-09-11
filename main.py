# main.py
import sys
from pathlib import Path
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Keep exactly what the user typed for the report line
    rel_path = sys.argv[1]

    # Resolve file relative to this script (works from any cwd)
    base = Path(__file__).resolve().parent
    file_path = Path(rel_path)
    if not file_path.is_absolute():
        file_path = (base / rel_path)

    text = get_book_text(file_path)

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
        if ch.isalpha():  # skip non-letters
            print(f"{ch}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

