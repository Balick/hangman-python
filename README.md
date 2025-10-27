# Hangman — Console Game
### Jetbrains python project
https://hyperskill.org/projects/69

A small Python console implementation of the classic Hangman game. The script selects a random word from a built-in list and asks the player to guess it one letter at a time with a limited number of attempts.

## Overview
- Language: Python 3.x
- Dependencies: only standard library modules (`random`, `string`)
- Player starts with 8 attempts to guess a randomly chosen secret word.
- Session score (wins / losses) is kept in memory while the program runs.

## Files
- hangman.py — the main script (use the provided code).

## How to run
1. Save the provided code to a file named `hangman.py`.
2. Run from the terminal:
   ```bash
   python3 hangman.py
   ```
3. Follow on-screen prompts:
   - Type `play` to start a new game.
   - Type `results` to display the current session scoreboard.
   - Type `exit` to quit.

## Game rules (as implemented)
- Possible secret words: `["python", "java", "swift", "javascript"]`.
- The player has 8 incorrect attempts allowed.
- Each turn the program prints the current guessed state (known letters and `-` for unknown).
- The program expects a single lowercase ASCII letter as input. Validation:
  - If input length ≠ 1 → "Please, input a single letter."
  - If input is not a lowercase ASCII letter → "Please, enter a lowercase letter from the English alphabet."
- If the guessed letter is in the word, all occurrences of that letter are revealed.
- If the letter was already guessed (correctly or incorrectly), the game prints "You've already guessed this letter."
- If the letter is not in the word, the player loses one attempt.
- If the player reveals the whole word before attempts run out → win.
- If attempts reach 0 → loss. (The current implementation returns an empty string on loss; the secret word is not revealed.)

## Code structure
- Global variables:
  - `words` — list of candidate words.
  - `success_nb`, `lost_nb` — session counters for wins and losses.
- Functions:
  - `get_user_input(guessed_letters)` — displays the current guessed state, reads and validates a single-letter input, returns the valid letter.
  - `play()` — runs one game: selects a word, loops until win or attempts exhausted, returns the word if guessed or an empty string on loss.
- Main loop:
  - Prints "H A N G M A N" and repeatedly prompts the user for `play`, `results`, or `exit`, updating and showing the scoreboard.

## Implementation details and notes
- The script uses:
  - `guessed_letters` list of characters for display.
  - `remaining_letters` list to track letters not yet revealed (removes each occurrence when guessed).
  - `fake_guessed_letters` set to track incorrect guesses already made.
- The condition that detects repeated guesses:
  ```
  elif user_input not in remaining_letters and user_input in secret_word or user_input in fake_guessed_letters:
  ```
  This is equivalent to:
  ```
  (user_input not in remaining_letters and user_input in secret_word) or (user_input in fake_guessed_letters)
  ```
  and handles both re-guessing a previously revealed letter and repeating a previously incorrect guess.

## Suggested improvements
- Reveal the secret word after a loss to give feedback.
- Persist the scoreboard to disk (JSON file or SQLite) so it survives program restarts.
- Add an ASCII-art hangman that updates with each incorrect attempt.
- Normalize uppercase input by applying `.lower()` automatically.
- Load a larger vocabulary from an external file to increase variety.
- Add CLI options (e.g., max attempts, word list path) using `argparse`.
- Add unit tests for input validation and game logic.

## Example session
```text
H A N G M A N
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: play

----
Input a letter: p
p---
Input a letter: y
py--
...
You guessed the word python!
You survived!
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: results
You won: 1 times.
You lost: 0 times.
```
