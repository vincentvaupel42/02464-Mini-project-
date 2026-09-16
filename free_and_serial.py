"""
RECALL EXPERIMENT
-----------------
Shows a chosen number of random 4-letter English words one at a time in a window.
Each word is shown for 'seconds' seconds, then the next one appears automatically.

Afterwards a box appears where you type the words you remember.
The program then shows which words you got right (with their serial position)
and which words were wrong (so you can spot spelling mistakes).

The only parameters you need to change are 'seconds' and 'NUM_WORDS' below.
"""

import tkinter as tk
import random

# ================== PARAMETERS YOU CAN CHANGE ==================
seconds = 2.0    # how many seconds each word is shown on screen
NUM_WORDS = 15   # how many words are drawn and shown per trial
# ==============================================================

# Word list with 100+ English 4-letter words
word_pool = [
    "that", "with", "this", "have", "from", "your", "they", "will", "just", "like",
    "what", "when", "more", "were", "time", "been", "some", "also", "them", "than",
    "good", "into", "make", "over", "then", "back", "want", "well", "said", "most",
    "much", "very", "even", "here", "need", "work", "year", "made", "take", "many",
    "life", "down", "last", "best", "such", "love", "home", "long", "look", "same",
    "used", "both", "come", "part", "find", "help", "high", "does", "game", "give",
    "next", "each", "must", "show", "feel", "sure", "team", "ever", "keep", "free",
    "away", "left", "city", "days", "name", "play", "real", "done", "care", "week",
    "case", "full", "live", "read", "told", "four", "hard", "mean", "once", "tell",
    "seen", "stop", "call", "head", "took", "came", "side", "went", "less", "line",
    "says", "open", "area", "face", "five", "kind", "hope", "news", "able", "book",
    "post", "talk", "fact", "guys", "half", "hand", "mind", "body", "food", "true",
    "lost", "room", "else", "girl", "john", "nice", "yeah", "york", "idea", "past",
    "move", "wait", "data", "late", "stay", "deal", "soon", "turn", "form", "fire",
    "easy", "near", "plan", "west", "kids", "list", "meet", "baby", "song", "word",
    "gave", "gets", "self", "cost", "held", "main", "road", "town", "fine", "hear",
    "rest", "term", "wife", "date", "goes", "land", "miss", "shot", "site", "eyes",
    "june", "club", "died", "film", "lead", "dead", "hold", "star", "test", "view",
    "hour", "wish", "gold", "gone", "july", "king", "bank", "east", "park", "role",
    "sent", "bill", "cool", "rate", "save", "blue", "fall", "fast", "felt", "size",
    "step", "page", "paid", "upon", "hate", "send", "vote", "lord", "born", "kill",
    "poor", "code", "door", "hair", "lose", "pick", "race", "seem", "sign", "walk",
    "loss", "ones", "safe", "goal", "huge", "okay", "ways", "base", "deep", "mark",
    "pass", "risk", "ball", "card", "dark", "mine", "note", "wall", "boys", "fans",
    "pain", "paul", "rock", "cold", "anti", "beat", "text", "join", "kept", "sort",
    "drop", "fair", "feet", "link", "sale", "tour", "jobs", "sell", "sold", "wide",
    "fear", "lady", "plus", "unit", "hurt", "rule", "none", "ship", "band", "cash",
    "lack", "wear", "luck", "rich", "skin", "thus", "fish", "glad", "grow", "trip",
    "cars", "laws", "male", "spot", "holy", "lots", "shop", "sick", "uses", "cell",
    "drug", "foot", "hall", "mass", "nine", "heat", "fell", "ride", "slow", "tree",
]

# ---------------- The program starts here ----------------
random.shuffle(word_pool)
chosen_words = word_pool[:NUM_WORDS]

# ---------- Part 1: show the words one at a time ----------
root = tk.Tk()
root.title("Recall experiment")
root.geometry("500x250")
# Place the window in the middle of the screen
root.eval('tk::PlaceWindow . center')

label = tk.Label(root, text="", font=("Helvetica", 40))
label.pack(expand=True)


def show_word(index):
    if index >= len(chosen_words):
        root.destroy()
        return
    label.config(text=chosen_words[index])
    root.after(int(seconds * 1000), show_word, index + 1)


# Small pause before the first word so the window has time to be drawn
root.after(4000, show_word, 0)
root.mainloop()


# ---------- Part 2: type in the words you remember ----------
# We store the words you type in this list (in the order you type them).
recalled_words = []

answer_root = tk.Tk()
answer_root.title("What did you see?")
answer_root.geometry("400x420")
answer_root.eval('tk::PlaceWindow . center')

info = tk.Label(answer_root, text="Type the words you saw\n(one per line):", font=("Helvetica", 14))
info.pack(pady=10)

# A multi-line text box you can type all your words into
text_box = tk.Text(answer_root, font=("Helvetica", 16), width=18, height=12)
text_box.pack(expand=True)
text_box.focus_set()


def done():
    # Read everything from the text box (from line 1, char 0, to the end)
    content = text_box.get("1.0", "end")
    # split() cuts the text into single words at every space and newline
    for word in content.split():
        recalled_words.append(word.lower())
    answer_root.destroy()


button = tk.Button(answer_root, text="Done", font=("Helvetica", 14), command=done)
button.pack(pady=10)

answer_root.mainloop()


# ---------- Part 3: compare and show the result ----------
correct = []   # list of (serial position, word) for words that were actually shown
wrong = []     # words you typed that were NOT shown (e.g. spelling mistakes)

for word in recalled_words:
    if word in chosen_words:
        position = chosen_words.index(word) + 1   # serial position: 1 = shown first
        correct.append((position, word))
    else:
        wrong.append(word)

# Sort the correct words by their serial position so the list is easy to read
correct.sort()

print("Words shown in this order:")
for pos, word in enumerate(chosen_words, start=1):
    print(f"{pos}. {word}")

print("\nCorrect words (with serial position):")
for position, word in correct:
    print(f"position {position}: {word}")

print("\nWrong words (not shown - check for spelling mistakes):")
for word in wrong:
    print(word)

print(f"\nYou remembered {len(correct)} of {len(chosen_words)} words correctly.")
