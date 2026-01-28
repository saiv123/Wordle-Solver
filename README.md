# Wordle-Solver

A Python tool to help you solve Wordle puzzles by filtering word possibilities based on color feedback from each guess.

## Overview

This solver uses a curated list of valid Wordle words and progressively eliminates possibilities based on the color feedback you receive:
- **Green (g)**: Letter is correct and in the right position
- **Yellow (y)**: Letter is in the word but wrong position
- **Gray (-)**: Letter is not in the word

## Requirements

- Python 3.x
- `wordles.json` - A JSON file containing a list of valid 5-letter words

## How to Use

1. Run the script:
   ```bash
   python Solver.py
   ```

2. Enter your guessed word when prompted

3. Enter the color feedback from Wordle:
   - `g` for green (correct position)
   - `y` for yellow (wrong position)
   - `-` for gray (not in word)
   
   Example: If you guessed "SLATE" and got Green-Gray-Yellow-Gray-Green, enter: `g-y-g`

4. The solver will display the remaining possible words

5. Continue guessing and providing feedback until you solve the puzzle

6. When asked "guessed?(y/n)", answer `y` to confirm you've solved it

## How It Works

The solver uses a filtering algorithm that:
1. **Removes words with gray letters** - Eliminates any word containing letters marked as gray
2. **Filters yellow letters** - Removes words where yellow letters are in the marked positions
3. **Checks green letters** - Only keeps words where green letters match the exact positions

## Example Workflow

```
What is the word you guessed? slate
What was the letter colors? g=green y=yellow '-'=gray: g----
[Remaining words matching: S at position 0, no other constraints...]
Guessed?(y/n): n
...
```

## Files

- `Solver.py` - Main solver script
- `wordles.json` - List of valid Wordle words
