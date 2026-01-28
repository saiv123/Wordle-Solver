from typing import List, Tuple
import json
with open("wordles.json", 'r') as f:
    word_list:List[str] = json.load(f)

green:List[Tuple[str, int]] = [('0', -1),('0', -2),('0', -3),('0', -4),('0', -5)]
yellow:List[Tuple[str, List[int]]] = []
gray:List[str] = []

# Sorts user input and categorizes letters into green, yellow, and gray lists
def sorting():
    guess = input("what is the word you guessed?:").lower()
    colors = input("what was the letter colors? g = green y = yellow '-' = gray:").lower()
    for i in range(5):
        c = colors[i]
        if c == 'g':
            green[i] = (guess[i],i)
        elif c == 'y':
            for l, p in yellow:
                if l  == guess[i]:
                    if i not in p:
                        p.append(i)
                    break
            else:
                yellow.append((guess[i],[i]))
        else:
            gray.append(guess[i])
    remove_word()
    print(word_list)

# Filters words based on letter position feedback (green/yellow/gray)
def remove_word():
    for w in word_list[:]:
        removed = False
        if any(c in w for c in gray):
            word_list.remove(w)
            continue
                
        for c,p in yellow:
            if any(w[i] == c for i in p):
                word_list.remove(w)
                removed = True
                break
            else:
                word_list.remove(w)
                removed = True
                break
        
        if removed : continue
        for c,p in green:
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