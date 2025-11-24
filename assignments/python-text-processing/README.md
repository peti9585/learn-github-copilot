# 📘 Assignment: Python Text Processing

## 🎯 Objective
Build a small toolkit for loading, cleaning, analyzing, and transforming plain-text files. You will practice Python string manipulation, file I/O, counting/frequency analysis, simple pattern searching, and basic command‑line interaction.

## 📝 Tasks

### 🛠️ String Cleanup & Character Stats

#### Description
Write functions to normalize text input and compute basic character statistics.

#### Requirements
Completed program should:

- Provide a `clean_text(text)` function that strips leading/trailing whitespace, normalizes internal spacing, and converts to lowercase.
- Provide a `count_characters(text)` function returning counts of total characters (excluding newlines), digits, whitespace, and punctuation.
- Demonstrate both functions on a sample multiline string in `main()`.

### 🛠️ File Loading & Word Counts

#### Description
Read a `.txt` file and produce word-level statistics.

#### Requirements
Completed program should:

- Implement `read_file(path)` returning the entire file contents as a string (handle FileNotFoundError gracefully).
- Implement `word_counts(text)` returning: total words, unique words, and a dictionary of word→frequency (case-insensitive, punctuation removed).
- Display the top 10 most frequent words with their counts.

### 🛠️ Pattern Search & Highlight

#### Description
Search for given keywords and highlight occurrences.

#### Requirements
Completed program should:

- Implement `search_keywords(text, keywords)` returning a dict of keyword→occurrence count.
- Print lines containing any keyword, with the keyword uppercased for visual highlight.
- Accept keywords via command-line argument `--keywords word1,word2,...`.

### 🛠️ Text Transformation CLI

#### Description
Provide simple transformations accessible through command-line options.

#### Requirements
Completed program should:

- Implement `wrap_lines(text, width=80)` that wraps long lines without breaking words.
- Implement `remove_stopwords(words, stopwords)` returning a filtered list.
- Support command-line args: `--file path`, `--wrap WIDTH`, `--stopwords file_with_stopwords`, and `--keywords list`.
- Output a summary report: character stats, top 10 words, keyword counts, and wrapped sample of first 5 lines.

## ✅ Deliverables
- Updated `starter-code.py` with all required functions and a `main()` demonstrating features.
- Ability to run: `python starter-code.py --file sample.txt --keywords data,python --wrap 60`

## 💡 Tips
- Use `str.translate` or `re` to strip punctuation.
- Consider using `collections.Counter` for word frequencies.
- Always handle missing files gracefully and provide friendly error messages.

## 🚀 Extension (Optional)
Add a `--export report.txt` option that saves the summary report to a file.

## 📅 Due Date
December 1, 2025

Good luck! Focus on writing clear, reusable functions and friendly output.
