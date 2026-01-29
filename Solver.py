from typing import List, Tuple
from collections import defaultdict
import json
with open("wordles.json", 'r') as f:
    word_list:List[str] = json.load(f)

green:List[Tuple[str, int]] = [('0', -1),('0', -2),('0', -3),('0', -4),('0', -5)]
yellow:List[Tuple[str, List[int]]] = []
gray:List[str] = []

# Sorts user input and categorizes letters into green, yellow, and gray lists
def sorting():
    guess = input("what is the word you guessed?: ").lower()
    colors = input("what was the letter colors? g = green y = yellow '-' = gray: ").lower()

    guess_counts = defaultdict(int)
    confirmed_counts = defaultdict(int)

    # ---- First pass: greens and yellows ----
    for i in range(5):
        letter = guess[i]
        c = colors[i]

        if c == 'g':
            green[i] = (letter, i)
            confirmed_counts[letter] += 1

        elif c == 'y':
            for l, p in yellow:
                if l == letter:
                    if i not in p:
                        p.append(i)
                    break
            else:
                yellow.append((letter, [i]))
            confirmed_counts[letter] += 1

        guess_counts[letter] += 1

    # ---- Second pass: grays (only truly absent letters) ----
    for i in range(5):
        if colors[i] != '-':
            continue

        letter = guess[i]

        # Only mark gray if the letter was never confirmed
        if confirmed_counts[letter] == 0:
            if letter not in gray:
                gray.append(letter)
    remove_word()
    print(word_list)

# Filters words based on letter position feedback (green/yellow/gray)
def remove_word():
    for w in word_list[:]:
        removed = False
        if any(c in w for c in gray):
            word_list.remove(w)
            continue
                
        for c, p in yellow:
            # must contain the letter somewhere
            if c not in w:
                word_list.remove(w)
                removed = True
                break

            # must NOT be in any forbidden position
            if any(w[i] == c for i in p):
                word_list.remove(w)
                removed = True
                break
        
        if removed : continue
        for c,p in green:
            if p < 0:
                continue
            if w[p] != c:
                word_list.remove(w)

sorting()
guess = input("guessed?(y/n)").lower()
word_guessed = False
if guess[0] == 'y':
    word_guessed = True
while not word_guessed:
    sorting()
    guess = input("guessed?(y/n)").lower()
    if guess[0] == 'y':
        word_guessed = True