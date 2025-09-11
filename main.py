#open/read books/frankenstein.txt
from pathlib import Path
def get_book_text(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
    
def main():
    # Path to frankenstein.txt relative to THIS file
    base = Path(__file__).resolve().parent
    path = base / "books" / "frankenstein.txt"   # adjust if your layout differs

    text = get_book_text(path)
    print(text)

if __name__ == "__main__":
    main()  

#count words
from stats import count_words