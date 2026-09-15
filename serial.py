"""
PRIMACY-EKSPERIMENT (ord-for-ord)
----------------------------------
Trækker 3 tilfældige sætninger og viser dem ord for ord, i den rigtige
rækkefølge inden for hver sætning. Der er en kort pause mellem sætningerne,
så deltageren kan mærke overgangen til en ny sætning.

Den eneste parameter du skal ændre, er 'tid' nedenfor.
"""

import tkinter as tk
import random

# ================== PARAMETER DU KAN ÆNDRE ==================
tid = 1  # antal sekunder hvert ORD vises på skærmen
pause_mellem_saetninger = 0.5  # sekunder tom skærm mellem sætninger
# ==============================================================

saetningsliste = [
    "You paint old fences eagerly", "She grow more patient today", "She drive blue trucks sadly",
    "He teach young kids bravely", "I save little money gently", "They fold clean shirts smoothly",
    "He stack wooden boxes bravely", "We draw simple maps slowly", "They guard quiet houses eagerly",
    "She bring fresh bread gently", "He teach young kids coldly", "I teach young kids slowly",
    "We clean small rooms kindly", "They read good books boldly", "You eat red apples slowly",
    "You build tall towers sadly", "She draw simple maps quickly", "They clean small rooms eagerly",
    "He write short stories happily", "She save little money loudly", "I carry heavy bags nervously",
    "We bake sweet cakes coldly", "We remain still quiet downstairs", "You dance whole nights easily",
    "I carry heavy bags boldly", "We clean small rooms roughly", "He eat red apples bravely",
    "He wash dirty dishes roughly", "He drink cold milk roughly", "He grow fresh herbs bravely",
    "He guard quiet houses loudly", "They watch funny movies gently", "He fix broken chairs boldly",
    "He bake sweet cakes calmly", "She open front doors boldly", "I teach young kids smoothly",
    "She cook hot soup roughly", "I stack wooden boxes easily", "You stack wooden boxes roughly",
    "She wear warm coats warmly", "She teach young kids slowly", "They dance whole nights kindly",
    "You save little money bravely", "You lose house keys nervously", "We write short stories smoothly",
    "I pack light bags quietly", "He guard quiet houses boldly", "I open front doors boldly",
    "He look so proud downstairs", "We sing happy songs quickly", "She find lost dogs slowly",
    "I ride green bikes coldly", "He pack light bags nervously", "He throw small balls gently",
    "She write short stories loudly", "They lose house keys sadly", "They bake sweet cakes eagerly",
    "They guard quiet houses roughly", "We visit local parks kindly", "We catch fast trains carefully",
    "I climb steep hills coldly", "We buy new phones roughly", "I save little money smoothly",
    "We watch funny movies boldly", "You appear still upset indoors", "I ride green bikes roughly",
    "We ride green bikes easily", "You lose house keys carefully", "They carry heavy bags smoothly",
    "They look quite nervous today", "He clean small rooms boldly", "I read good books bravely",
    "They carry heavy bags quietly", "They fix broken chairs happily", "We buy new phones slowly",
    "I draw simple maps roughly", "We cook hot soup slowly", "He dance whole nights gently",
    "He wash dirty dishes gently", "You plant young trees eagerly", "He ride green bikes quietly",
    "She drive blue trucks calmly", "She teach young kids nervously", "She draw simple maps smoothly",
    "I sound very worried indoors", "I count small coins sadly", "I teach young kids warmly",
    "You ride green bikes smoothly", "You cook hot soup proudly", "We become so angry tonight",
    "They climb steep hills carefully", "I close back windows nervously", "We fold clean shirts easily",
    "He teach young kids loudly", "They teach young kids sadly", "I carry heavy bags gently",
    "I bake sweet cakes roughly", "I drink cold milk warmly", "She bake sweet cakes proudly",
    "He shape soft clay quickly", "I stack wooden boxes warmly", "I close back windows boldly",
    "He stack wooden boxes boldly", "He plant young trees proudly", "She draw simple maps quietly",
    "He ride green bikes coldly", "We count small coins carefully", "They cook hot soup slowly",
    "She watch funny movies smoothly", "You remain still quiet tonight", "She drive blue trucks roughly",
    "He write short stories quickly", "I drink cold milk smoothly", "He drink cold milk sadly",
    "He wear warm coats smoothly", "We build tall towers smoothly", "They draw simple maps kindly",
    "They lose house keys quietly", "He watch funny movies smoothly", "You drink cold milk carefully",
    "She bring fresh bread loudly", "I cook hot soup eagerly", "She draw simple maps nervously",
    "They grow fresh herbs nervously", "He eat red apples happily", "I build tall towers kindly",
    "She lose house keys kindly", "We open front doors sadly", "I drink cold milk quickly",
    "We climb steep hills gently", "They find lost dogs roughly", "She bring fresh bread smoothly",
    "She climb steep hills coldly", "She wash dirty dishes slowly", "I drive blue trucks quickly",
    "We fix broken chairs warmly", "We count small coins calmly", "She sound very worried today",
    "He ride green bikes boldly", "She grow more patient upstairs", "We save little money easily",
    "She lose house keys boldly", "You stack wooden boxes nervously", "We write short stories slowly",
    "We fold clean shirts nervously", "She sing happy songs nervously", "You save little money quickly",
    "He fix broken chairs calmly", "You stack wooden boxes slowly", "She read good books loudly"
]
ANTAL_SAETNINGER = 3  # hvor mange sætninger der trækkes og vises pr. forsøg

# ---------------- Programmet starter her ----------------
random.shuffle(saetningsliste)
valgte_saetninger = saetningsliste[:ANTAL_SAETNINGER]

# Byg en flad liste af "hændelser": hvert ord, samt en tom "pause"-hændelse
# mellem sætningerne, uden at blande ord fra to forskellige sætninger sammen.
visnings_sekvens = []  # liste af (tekst, varighed_i_sekunder)
for i, saetning in enumerate(valgte_saetninger):
    for ord in saetning.split():
        visnings_sekvens.append((ord, tid))
    if i < len(valgte_saetninger) - 1:
        visnings_sekvens.append(("", pause_mellem_saetninger))

root = tk.Tk()
root.title("Primacy-eksperiment")
root.geometry("500x250")
root.eval('tk::PlaceWindow . center')

label = tk.Label(root, text="", font=("Helvetica", 40), wraplength=450, justify="center")
label.pack(expand=True)


def vis_ord(index):
    if index >= len(visnings_sekvens):
        root.destroy()
        return
    tekst, varighed = visnings_sekvens[index]
    label.config(text=tekst)
    root.after(int(varighed * 1000), vis_ord, index + 1)


# Lille pause før første ord, så vinduet når at blive tegnet
root.after(1000, vis_ord, 0)
root.mainloop()

print("\nSætninger vist i denne rækkefølge (primacy):")
for pos, saetning in enumerate(valgte_saetninger, start=1):
    print(f"{pos}. {saetning}")