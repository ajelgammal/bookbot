# stats.py
def get_num_words(text: str) -> int:
    return len(text.split())

def get_char_counts(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for ch in text.lower():          # include spaces, punctuation, newlines, etc.
        counts[ch] = counts.get(ch, 0) + 1
    return counts
