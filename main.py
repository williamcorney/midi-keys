import rtmidi2
import time
import random
from colorama import Fore, Back, Style
import os
majorscales = ['2','2','1','2','2','2','1']


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


keys = ["C major","G major","D major","A major","E major","B major","F# major","D flat major", "A flat major","E flat major","B flat major","F major","A minor","E minor","B minor","F# minor","G# minor","B flat minor","D# minor","F minor", "C minor","G minor","D minor"]
print (len(keys))

#lottery1 = random.randint(0,10)
os.system('clear')
lottery1 = random.randint(0,23)
print ('Enter the notes of ' + keys[lottery1])
currentkey = keys[lottery1]
scaleslist = {
    "C major": ["C", "D", "E",
              "F", "G", "A", "B", "C"],
    "G major": ["G", "A", "B",
                "C", "D", "E", "F#", "G"],
    "D major": ["D", "E", "F#",
                "G", "A", "B", "C#", "D"],
    "A major": ["A", "B",
                "C#", "D", "E", "F#", "G#","A"],
    "E major": ["E", "F#",
                "G#", "A", "B", "C#", "D#", "E"],
    "B major": ["B", "C#",
                "D#", "E", "F#", "G#", "A#", "B"],
    "F# major": ["F#", "G#",
                "A#", "B", "C#", "D#", "F","F#"],
    "D flat major": ["C#", "D#", "F",
                "F#", "G#", "A#", "C", "C#"],
    "A flat major": ["G#", "A#", "C",
                "C#", "D#", "F", "G","G#"],
    "E flat major": ["D#", "F", "G",
                "G#", "A#", "C", "D", "D#"],
    "B flat major": [
                "A#", "C", "D", "D#", "F", "G","A", "A#"],
    "E major": ["E", "F#",
                "G#", "A", "B", "C#", "D#", "E"],
    "F major": ["F", "G",
                "A", "A#", "C", "D", "E", "F"],
"A minor": ["A", "B","C", "D", "E", "F", "G", "A"],
"E minor": ["E", "F#", "G", "A", "B", "C", "D", "E"],

"B minor":  ["B",  "C#","D", "E", "F#", "G", "A", "B"],
"F# minor": ["F#", "G#", "A", "B", "C#", "D", "E", "F#"],
"C# minor": ["C#", "D#", "E", "F#", "G#", "A", "B", "C#"],
"G# minor": ["G#", "A#", "B", "C#", "D#", "E", "F#", "G#"],
"B flat minor": ["A#", "C",  "C#", "D#", "F", "F#", "G#", "A#"],
"D# minor": ["D#", "F",  "F#", "G#", "A#", "B", "C#", "D#"],
"F minor": ["F", "G",  "G#", "A#", "C", "C#", "D#", "F"],
"C minor": ["C", "D",  "D#", "F", "G", "G#", "A#", "C"],
"G minor": ["G", "A",  "A#", "C", "D", "D#", "F", "G"],
"D minor": ["D", "E",  "F", "G", "A", "A#", "C", "D"],
}





#print (scaleslist['C major'][0])
#print (scaleslist[currentkey])
# C D E F G A B
#
# C 0
# D 2
# E 3
# F 4
# G 5
# A 6
# B 7


def number_to_note(number: int) -> tuple:
    octave = number // NOTES_IN_OCTAVE
    assert octave in OCTAVES, errors['notes']
    assert 0 <= number <= 127, errors['notes']
    note = NOTES[number % NOTES_IN_OCTAVE]

    return note, octave

NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
OCTAVES = list(range(11))
NOTES_IN_OCTAVE = len(NOTES)

midi_in = rtmidi2.MidiIn()
midi_in.open_port(0)




#print (keys[lottery])

CMAJOR = ["C","D","E","F","G","A","B","C"]
#print (CMAJOR[3])
interval = 0

while True:
    message = midi_in.get_message()
    if message:
        #print (message)
        type = message[0]
        if type == 144:

            value = number_to_note (message[1])
            # print (value[0])
            activekey = value[0]
            #correctkey = CMAJOR [interval]

            correctkey = (scaleslist[currentkey][interval])

            if activekey == correctkey :
                print ( Fore.GREEN + str(interval +1 ) + ' - ' + activekey)
                interval += 1
            else:
                #print (Fore.RED + str(interval +1) + ' - ' + activekey)
                interval = 0

                os.system('clear')
                print('Enter the notes of ' + keys[lottery1])
                currentkey = keys[lottery1]
                correctkey = (scaleslist[currentkey][interval])





        if interval ==8 :
            lottery1 = random.randint(0, 23)
            print('Enter the notes of ' + keys[lottery1])
            currentkey = keys[lottery1]
            interval = 0



    else:
        time.sleep(0.01)



