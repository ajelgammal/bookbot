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
from pathlib import Path

def get_book_text(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def count_words(text: str) -> int:
    # Split on any whitespace and count
    return len(text.split())

def main():
    base = Path(__file__).resolve().parent
    path = base / "books" / "frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()