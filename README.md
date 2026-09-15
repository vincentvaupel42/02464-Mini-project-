# 02464-Mini-project-

**Free recall experiment:**
This code is written to be run in a Jupyter Notebook. It displays a series of random 4-letter English words, one at a time, in a simple window, and the participant is asked to try to remember the words as they are shown. 

Before running the notebook, make sure the following packages are available: tkinter(to show the pop-up window) and random(for making a fair choice on which words are shown).

Two parameters can be adjusted at the top of the script: "Time", which sets the number of seconds each word is displayed on screen, and "Total_words", which sets the total number of words shown during the experiment. To change either parameter, edit the value directly in the code cell before running it.

To run the experiment, open the notebook in Jupyter, make sure "Time" and "Total_words" are set to the desired values, and run the code. A window will open automatically after a 4-second delay, which gives time to open the window in fullscreen before first word appears. The window then displays one word at a time at the interval set by "Time", until "Total_words" have been shown, after which it closes automatically. The order in which the words were shown is then printed in the notebook output directly below the code cell, and this list can be used to compare against the words the participant is able to recall afterward.

After each run, the number of correctly recalled words out of the "Total_words" shown is noted down in an Excel sheet, so that the results across participants and runs can be used for statistical analysis afterward.

The experiment was replicated three times (participant had 5 minute break between each run) where following changes were made:

0.5 second interval: "Time" was set to 0.5.

30 second pause: the participant was given a 30-second pause before recall.

Interference task pause: instead of a passive pause, the participant was asked to recite the 3-times table before recall.

For each replication, the number of correctly recalled words is noted down in the Excel sheet in the same way as described above, so the results from all runs can be compared statistically afterward.


**Serial recall experiment:**
This experiment is run in the same Jupyter Notebook and uses the same libraries as described above. Instead of a random word list, the word list now consists of sentences, where 2 full sentences of 5 words each are used, but the words are still shown one at a time, in the same way as before.

The participant is then asked to recall the words in the correct order, and the result is noted down in the Excel file.

The experiment is then repeated 3 more times, each time changing one condition:

3 sentences: the word list is changed to consist of 3 full sentences of 5 words each instead of 2.
Finger tapping: the participant taps their fingers on the table while the words are being shown.
Verbal suppression: the participant repeatedly says "bla bla bla" out loud while the words are being shown.

For each of the 4 runs, the participant's recall is noted down in the Excel file in the same way as described above, so the results can be compared statistically afterward.




