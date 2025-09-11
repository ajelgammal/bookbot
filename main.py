# main.py
from pathlib import Path
from stats import get_num_words, get_char_counts

def get_book_text(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    base = Path(__file__).resolve().parent
    path = base / "books" / "frankenstein.txt"
    text = get_book_text(path)

    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    char_counts = get_char_counts(text)
    print(char_counts)  # prints the dictionary of character -> count

if __name__ == "__main__":
    main()

