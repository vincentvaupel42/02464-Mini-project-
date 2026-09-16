"""
PRIMACY-EKSPERIMENT
--------------------
Viser 20 tilfældige 4-bogstavs engelske ord ét ad gangen i et vindue.
Hvert ord vises i 'tid' sekunder, derefter kommer det næste automatisk.

Den eneste parameter du skal ændre, er 'tid' nedenfor.
"""

import tkinter as tk
import random

# ================== PARAMETER DU KAN ÆNDRE ==================
tid = 2  # antal sekunder hvert ord vises på skærmen
# ==============================================================

# Ordliste med 100+ engelske ord på 4 bogstaver
ordliste = [
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

ANTAL_ORD = 15  # hvor mange ord der trækkes og vises pr. forsøg

# ---------------- Programmet starter her ----------------
random.shuffle(ordliste)
valgte_ord = ordliste[:ANTAL_ORD]

root = tk.Tk()
root.title("Primacy-eksperiment")
root.geometry("500x250")
#Place root in middle of screen
root.eval('tk::PlaceWindow . center')

label = tk.Label(root, text="", font=("Helvetica", 40))
label.pack(expand=True)


def vis_ord(index):
    if index >= len(valgte_ord):
        root.destroy()
        return
    label.config(text=valgte_ord[index])
    root.after(int(tid * 1000), vis_ord, index + 1)


# Lille pause før første ord, så vinduet når at blive tegnet
root.after(4000, vis_ord, 0)
root.mainloop()

print("\nOrd vist i denne rækkefølge:")
for pos, ord in enumerate(valgte_ord, start=1):
    print(f"{pos}. {ord}")
