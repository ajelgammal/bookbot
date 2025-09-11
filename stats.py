# stats.py
from typing import Dict, List

def get_num_words(text: str) -> int:
    return len(text.split())

def get_char_counts(text: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for ch in text.lower():  # include spaces/punct/newlines; all lowercased
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_on(item: dict) -> int:
    return item["num"]

def sort_char_counts(counts: Dict[str, int]) -> List[dict]:
    items = [{"char": ch, "num": n} for ch, n in counts.items()]
    items.sort(reverse=True, key=sort_on)  # greatest -> least
    return items