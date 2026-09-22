"""
Chunking experiment (ord-for-ord)
Shows 2 random sentences comprised of 5 words each with varying length to show effects of chunking.
Short break between sentences to state end and beginning of sentence.
"""

import tkinter as tk
import random

# Parameters
tid = 1 
pause_mellem_saetninger = 0.5

saetningsliste = [
    "I polish brass lanterns carefully",
    "You measure narrow doorways quietly",
    "He repairs broken bicycles promptly",
    "She carries woven baskets gracefully",
    "We observe distant planets patiently",
    "They deliver sealed parcels securely",
    "I arrange winter flowers neatly",
    "You explore coastal caves smoothly",
    "He collects rare stamps curiously",
    "She examines ancient maps thoroughly",
    "We prepare spicy noodles cheerfully",
    "They discover hidden trails briskly",
    "I practice difficult chords steadily",
    "You organize digital photos politely",
    "He sketches city rooftops boldly",
    "She plants young saplings gently",
    "We compare market prices efficiently",
    "They assemble wooden shelves closely",
    "I calculate monthly budgets skillfully",
    "You inspect safety helmets calmly",
    "He navigates foggy harbors accurately",
    "She records bird songs softly",
    "We decorate ceramic bowls creatively",
    "They transport museum artifacts safely",
    "I monitor river levels diligently",
    "You balance stacked plates evenly",
    "He sorts recycling materials warmly",
    "She guides visiting tourists respectfully",
    "We restore vintage furniture properly",
    "They test wireless sensors reliably",
    "I fold linen napkins methodically",
    "You read science journals thoughtfully",
    "He paints garden gates eagerly",
    "She builds sand castles delicately",
    "We pack camping supplies regularly",
    "They wash muddy boots attentively",
    "I write travel notes confidently",
    "You cook tomato soup slowly",
    "He drives delivery vans quickly",
    "She solves logic puzzles silently",
    "We clean office windows openly",
    "They watch nature documentaries together",
    "I climb rocky slopes cautiously",
    "You water kitchen herbs daily",
    "He throws practice balls outside",
    "She chooses painted fabrics carefully",
    "We visit nearby islands often",
    "They catch morning trains early",
    "I charge camera batteries overnight",
    "You open heavy curtains gently",
    "He bakes oatmeal cookies expertly",
    "She finds missing gloves downstairs",
    "We sing campfire songs loudly",
    "They move storage crates indoors",
    "I sharpen drawing pencils slowly",
    "You fix leaking faucets properly",
    "He feeds stray kittens outside",
    "She sews costume buttons neatly",
    "We cross stone bridges safely",
    "They harvest ripe pears today",
    "I trace winding footpaths patiently",
    "You check train schedules online",
    "He mixes fruit smoothies daily",
    "She mends torn curtains upstairs",
    "We launch paper airplanes together",
    "They sweep porch steps thoroughly",
    "I label archive boxes clearly",
    "You tune acoustic guitars carefully",
    "He rinses paint brushes afterward",
    "She climbs spiral staircases slowly",
    "We review class assignments nightly",
    "They plant vegetable seeds outside",
    "I browse used bookstores happily",
    "You hang framed posters evenly",
    "He rolls fresh pastry skillfully",
    "She checks engine oil weekly",
    "We solve crossword clues together",
    "They buy seasonal tickets online",
    "I mow overgrown grass regularly",
    "You wrap birthday presents neatly",
    "He draws wildlife scenes beautifully",
    "She boils pasta water gently",
    "We share picnic blankets generously",
    "They count donation coins carefully",
    "I dust library shelves quietly",
    "You clean computer screens gently",
    "He rakes fallen leaves outside",
    "She files legal papers properly",
    "We repair garden benches together",
    "They light scented candles nightly",
    "I gather fallen branches nearby",
    "You practice swimming strokes daily",
    "He orders vegetarian lunches politely",
    "She prints meeting agendas early",
    "We study volcanic rocks closely",
    "They climb forest towers slowly",
    "I empty recycling bins weekly",
    "You deliver fresh bread promptly",
    "He measures fabric lengths carefully",
    "She paints watercolor portraits beautifully",
    "We fix loose hinges quickly",
    "They carry folding chairs inside",
    "I watch cloud formations quietly",
    "You plant balcony tomatoes outside",
    "He updates project files regularly",
    "She stacks clean towels neatly",
    "We sort laundry colors carefully",
    "They repair sailing ropes patiently",
    "I fill water bottles daily",
    "You slice crisp apples thinly",
    "He marks calendar dates clearly",
    "She writes thank-you cards warmly",
    "We build model rockets together",
    "They guide museum visitors politely",
    "I check weather forecasts often",
    "You trim basil leaves gently",
    "He saves spare change monthly",
    "She knits woolen scarves patiently",
    "We photograph street murals downtown",
    "They collect beach shells happily",
    "I clean dusty mirrors carefully",
    "You close bedroom shutters quietly",
    "He waters thirsty roses daily",
    "She reads mystery novels nightly",
    "We visit historic castles often",
    "They paint theater backdrops creatively",
    "I carry groceries upstairs slowly",
    "You press fresh shirts neatly",
    "He checks bike tires weekly",
    "She plans weekend trips early",
    "We make lemon tarts together",
    "They draw comic panels skillfully",
    "I remove old stickers carefully",
    "You send birthday invitations promptly",
    "He feeds colorful fish daily",
    "She keeps detailed records organized",
    "We pack beach towels lightly",
    "They clean kitchen counters thoroughly",
    "I inspect bridge supports closely",
    "You copy study notes accurately",
    "He opens shop doors early",
    "She chooses spring jackets thoughtfully",
    "We wash painted mugs gently",
    "They deliver library books promptly",
    "I turn compost piles weekly",
    "You bake cinnamon rolls slowly",
    "He trims hedge branches carefully",
    "She organizes art supplies neatly",
    "We visit local markets Saturdays",
    "They test emergency alarms monthly",
]

ANTAL_SAETNINGER = 2

random.shuffle(saetningsliste)
valgte_saetninger = saetningsliste[:ANTAL_SAETNINGER]

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

root.after(1000, vis_ord, 0)
root.mainloop()

print("\nSætninger vist i denne rækkefølge (primacy):")
for pos, saetning in enumerate(valgte_saetninger, start=1):
    print(f"{pos}. {saetning}")
