# 02464-Mini-project-
This project contains two Python files:
- **Recall/serial recall file**: used for both the free recall and serial recall experiments. Each sub-experiment is run 5 times.
- **Chunking file**: a separate Python file that shows sentences instead of random words. It uses the same libraries as the first file.

## Requirements
Both scripts use the following modules, which are part of Python's standard library (no separate installation should be needed):
- `tkinter`: shows the pop-up window
- `random`: picks which words are shown

## Free recall experiment
The script displays a series of random 4-letter English words, one at a time, in a simple window. The participant tries to remember as many of the words as possible. They do not need to recall them in any particular order, only how many they remember in total.

**Parameters**
Two parameters can be adjusted at the top of the script. To change either one, edit its value directly in the code before running.
- `SECONDS`: number of seconds each word is displayed on screen
- `NUM_WORDS`: total number of words shown during the experiment

### Running the experiment
1. Open the Python file and set `SECONDS` and `NUM_WORDS` to the desired values.
2. Run the code. A window opens automatically after a 4-second delay, which gives you time to make it fullscreen before the first word appears.
3. The window shows one word at a time, at the interval set by `SECONDS`, until `NUM_WORDS` words have been shown. It then closes automatically.
4. The list of words in the order they were shown is printed. Use it to check the participant's answers. Every word recalled correctly counts as one point, regardless of order.
After each run, note the number of correctly recalled words (out of `NUM_WORDS`) in an Excel sheet so results across participants and runs can be analysed statistically.

### Conditions
The experiment was replicated with the following changes. The participant had a minimum 5-minute break between runs.
- **0.5 second interval**: `SECONDS` was set to 0.5.
- **30-second pause**: the participant waited 30 seconds before recall.
- **Interference task pause**: instead of a passive pause, the participant recited the 3-times table before recall.
For each condition, the number of correctly recalled words is recorded in the Excel sheet in the same way, so all runs can be compared statistically afterwards.

## Serial recall experiment
This experiment uses the same Python file and libraries as the free recall experiment. The following conditions are used:
- **Finger tapping**: the participant taps their fingers on the table while the words are being shown.
- **Verbal suppression**: the participant repeatedly says "bla bla bla" out loud while the words are being shown.

## Chunking experiment
This experiment uses a separate Python file with the same libraries. Instead of a random word list, the list consists of **2 full sentences of 5 words each**. The words are still shown one at a time, in the same way as before.

The participant is asked to recall the words regardless of the order, and the result is recorded in the Excel file.

The participant's recall is recorded for each of the 4 runs in the same way as above, so results can be compared statistically afterwards.



