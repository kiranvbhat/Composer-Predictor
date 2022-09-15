# Kiran Bhat
# CS 109
# This program attempts to predict if Bach or Mozart composed a given mystery piece, using a method similar to the
# Federalist Papers example in CS 109. See writeup for more info about the probability theory.

import mido
import os
import math
import pandas as pd
import matplotlib.pyplot as plt

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
OCTAVE_LEN = 12


# This function takes in a midi number and returns its respective note notation
# ex) MIDI number 60 represents a middle C (C4), so: number_to_note(60) -> 'C4'
def num_to_note(num):
    octave = (num // OCTAVE_LEN) - 1
    note_letter = NOTES[(num % OCTAVE_LEN)]
    note = note_letter + str(octave)
    return note


# This function takes in a note dictionary (note: number of occurrences of that note) and MIDI file, then updates that
# note dictionary with notes read from the given MIDI file
def update_note_dict(note_dict, mid):
    for i in range(1, len(mid.tracks)):
        for msg in mid.tracks[i]:
            try:
                note = msg.note
                note_dict[note] = note_dict.get(note, 0) + 1  # note_dict.get(msg.note) returns 0 if note not in dict

            # first few lines of mid.tracks[i] don't contain note data (msg.note results in error), this skips those
            except AttributeError:
                continue
        # print_note_dict(note_dict)


# This function takes in a note dictionary, then converts it into a probability dictionary (note: probability of note)
def make_prob_dict(note_dict):
    num_notes = sum(note_dict.values())
    prob_dict = {note: val / num_notes for note, val in note_dict.items()}
    return prob_dict


# Given the name of a folder containing MIDI files, this function generates a dictionary for the probability of each
# note being played.
def generate_prob_dict(folder_name):
    file_list = sorted(os.listdir(folder_name))
    note_dict = {}
    # i = 0 (to loop thru array of key signatures)
    for file in file_list:
        if file == ".DS_Store":
            continue
        file_path = folder_name + "/" + file
        print(file_path)
        mid = mido.MidiFile(file_path, clip=True)
        if folder_name == "bach-training":
            update_note_dict(note_dict, mid)
        elif folder_name == "mozart-training":
            update_note_dict(note_dict, mid)
        else:
            print("Invalid Composer")
            return {}

    total_notes_in_dict = sum(note_dict.values())
    print("Total notes in dictionary: " + str(total_notes_in_dict))
    prob_dict = make_prob_dict(note_dict)
    return prob_dict

# ----------------------------------------------------------------------------------------------------------------------


# This function takes in a MIDI file and produces a list of the notes stored in the file
def make_note_list(mid):
    # key = mid.tracks[0].key
    note_list = []
    for i in range(1, len(mid.tracks)):
        for msg in mid.tracks[i]:
            try:
                note = msg.note
                note_list.append(note)
            # first few lines of mid.tracks[i] don't contain note data (msg.note results in error), this skips those
            except AttributeError:
                continue
    return note_list


# This function prints a note dictionary or note probability dictionary, but prints the letter+octave form of the note
# instead of the MIDI number, to improve readability
def print_note_dict(note_dict):
    printed_note_dict = {}
    for number in note_dict.keys():
        printed_note_dict[num_to_note(number)] = note_dict[number]
    print(printed_note_dict)


# This function takes in a probability dictionary and displays a bar chart (x-axis: notes, y-axis: probability).
# It also accepts a title for the chart to display.
def plot_probabilities(prob_dict, title):
    keys_for_plot = []
    probs_for_plot = []
    for i in range(21, 108):
        keys_for_plot.append(i)
        probs_for_plot.append(prob_dict.get(i, 0))

    plotdata = pd.DataFrame(
        {"probability": probs_for_plot}, index=keys_for_plot)
    # Plot a bar chart
    plotdata.plot(kind="bar")
    plt.title(title)
    plt.show()


# ----------------------------------------------------------------------------------------------------------------------

# This program attempts to predict if Bach or Mozart composed a given mystery piece, using a method similar to the
# Federalist Papers example in CS 109. See writeup for more info about the probability theory.
def main():
    # generate dictionaries for the probability of each music note
    bach_prob_dict = generate_prob_dict("bach-training")
    mozart_prob_dict = generate_prob_dict("mozart-training")

    # create list of notes in piece by mystery composer
    mystery_piece = "testing/mozart.mid"
    mystery_mid = mido.MidiFile(mystery_piece, clip=True)
    mystery_note_list = make_note_list(mystery_mid)

    # now compute the log of this ratio: P(piece | Bach) / P(piece | Mozart)
    log_sum_bach = 0
    log_sum_mozart = 0
    for note in mystery_note_list:
        log_sum_bach += math.log(bach_prob_dict.get(note, 1 / 145234))  # if note not in dict, prob is ~0 (>0 b/c log)
        log_sum_mozart += math.log(mozart_prob_dict.get(note, 1 / 300050))

    # print the results
    print("------------------RESULTS------------------")
    print("Bach log sum: " + str(log_sum_bach))
    print("Mozart log sum: " + str(log_sum_mozart))

    composer = "Bach" if (log_sum_bach > log_sum_mozart) else "Mozart"
    print("Mystery Composer: " + composer)

    # ------------------ Plotting probabilities ----------------------

    plot_probabilities(bach_prob_dict, "Bach")
    plot_probabilities(mozart_prob_dict, "Mozart")


if __name__ == '__main__':
    main()
