# 📘 Assignment: Hangman Game

## 🎯 Objective
Build a classic word-guessing game that strengthens your skills with strings, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Core Game Implementation

#### Description
Create an interactive Hangman game. The program chooses a secret word and the player guesses one letter at a time until they either reveal the full word or run out of attempts.

#### Requirements
Completed program should:
- Store a list of at least 10 possible words and randomly select one each round
- Display current progress using underscores for unknown letters (e.g. h _ n g m a n)
- Accept single-letter guesses (ignore repeats; prompt again if invalid)
- Track and show remaining incorrect attempts
- Show letters already guessed
- End with a clear win or loss message revealing the word
- Offer option to play again without restarting the script

Optional Enhancements (try these after core requirements):
- ASCII art gallows updating each wrong guess
- Difficulty levels that adjust allowed attempts
- Load words from an external text file

Learning Note: Test edge cases (repeated letters, non-alpha input, case-insensitivity) to build robust logic.
