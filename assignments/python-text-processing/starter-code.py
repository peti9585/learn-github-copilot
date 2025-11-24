import argparse
import re
from collections import Counter
from pathlib import Path

PUNCT_PATTERN = re.compile(r"[\.,!?:;\-\(\)\[\]\{\}\"'`]")


def clean_text(text: str) -> str:
    text = text.strip()
    # Collapse internal whitespace to single spaces
    text = re.sub(r"\s+", " ", text)
    return text.lower()


def count_characters(text: str) -> dict:
    stats = {
        "total": 0,
        "digits": 0,
        "whitespace": 0,
        "punctuation": 0,
    }
    for ch in text:
        if ch == "\n":
            continue
        stats["total"] += 1
        if ch.isdigit():
            stats["digits"] += 1
        elif ch.isspace():
            stats["whitespace"] += 1
        elif PUNCT_PATTERN.match(ch):
            stats["punctuation"] += 1
    return stats


def read_file(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def tokenize(text: str) -> list:
    cleaned = PUNCT_PATTERN.sub(" ", text)
    cleaned = cleaned.lower()
    return [t for t in cleaned.split() if t]


def word_counts(text: str) -> tuple:
    tokens = tokenize(text)
    counter = Counter(tokens)
    total = len(tokens)
    unique = len(counter)
    return total, unique, counter


def search_keywords(text: str, keywords: list) -> dict:
    lowered = text.lower()
    counts = {}
    for kw in keywords:
        kw_l = kw.lower().strip()
        if not kw_l:
            continue
        counts[kw_l] = lowered.count(kw_l)
    return counts


def highlight_lines(text: str, keywords: list) -> list:
    lines = text.splitlines()
    result = []
    for line in lines:
        original = line
        for kw in keywords:
            pattern = re.compile(re.escape(kw), re.IGNORECASE)
            original = pattern.sub(lambda m: m.group(0).upper(), original)
        if any(kw.lower() in line.lower() for kw in keywords):
            result.append(original)
    return result


def wrap_lines(text: str, width: int = 80) -> str:
    words = text.split()
    lines = []
    current = []
    current_len = 0
    for w in words:
        if current_len + len(w) + (0 if not current else 1) > width:
            lines.append(" ".join(current))
            current = [w]
            current_len = len(w)
        else:
            current.append(w)
            current_len += len(w) + (0 if not current else 1)
    if current:
        lines.append(" ".join(current))
    return "\n".join(lines)


def remove_stopwords(words: list, stopwords: set) -> list:
    return [w for w in words if w not in stopwords]


def load_stopwords(path: str) -> set:
    if not path:
        return set()
    try:
        content = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return set()
    return {w.strip().lower() for w in content.splitlines() if w.strip()}


def summary_report(text: str, width: int, keywords: list, stopwords: set) -> str:
    cleaned = clean_text(text)
    stats = count_characters(cleaned)
    total_words, unique_words, freq = word_counts(cleaned)
    filtered_tokens = remove_stopwords(tokenize(cleaned), stopwords)
    top10 = freq.most_common(10)
    kw_counts = search_keywords(cleaned, keywords)
    wrapped_sample = wrap_lines("\n".join(text.splitlines()[:5]), width)
    highlighted = highlight_lines(text, keywords)
    lines = [
        "=== Text Summary ===",
        f"Characters: total={stats['total']} digits={stats['digits']} whitespace={stats['whitespace']} punctuation={stats['punctuation']}",
        f"Words: total={total_words} unique={unique_words} after_stopword_filter={len(filtered_tokens)}",
        "Top 10 words: " + ", ".join(f"{w}:{c}" for w, c in top10),
        "Keyword counts: " + ", ".join(f"{k}:{v}" for k, v in kw_counts.items()),
        "--- Highlighted Lines (keywords) ---",
    ] + highlighted + [
        "--- Wrapped Sample (first 5 lines) ---",
        wrapped_sample,
    ]
    return "\n".join(lines)


def parse_args():
    parser = argparse.ArgumentParser(description="Python Text Processing Toolkit")
    parser.add_argument("--file", help="Path to input text file", required=False)
    parser.add_argument("--keywords", help="Comma-separated keywords", required=False, default="")
    parser.add_argument("--wrap", help="Wrap width", type=int, default=80)
    parser.add_argument("--stopwords", help="Stopwords file", required=False, default="")
    return parser.parse_args()


def main():
    args = parse_args()
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()] if args.keywords else []
    stopwords = load_stopwords(args.stopwords)

    sample_text = """Python is Fun!\nText processing allows you to clean, transform, and analyze data.\nPunctuation & Whitespace handling are essential.\nPractice makes progress.\nWrite clear, reusable code."""

    file_text = read_file(args.file) if args.file else sample_text

    report = summary_report(file_text, args.wrap, keywords, stopwords)
    print(report)


if __name__ == "__main__":
    main()
