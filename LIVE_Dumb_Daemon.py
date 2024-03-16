import sys
import os
import time
import rtmidi
import configparser

os.system("cls" if os.name == "nt" else "clear")
print("Starting...")

synthConfig=configparser.ConfigParser()

synthConfig.read("synth.cfg")

inDev=synthConfig["MIDI"]["In"]
outDev=synthConfig["MIDI"]["Out"]

midiout = rtmidi.MidiOut()
midiin = rtmidi.MidiIn()

class MidiInHandler:
    def __init__(self, midiOut):
        self.midiOut = midiOut

    def __call__(self, event, *args):
        event, delta = event
        self.midiOut.send_message(event)

try:
    midiin.open_port(int(inDev))
    midiout.open_port(int(outDev))
except RuntimeError:
    clearScreen()
    input("Could not open one\nor more MIDI ports.")
    sys.exit()

# auditory confirmation of handler start
midiout.send_message([0x99, 53, 112])
time.sleep(0.125)
midiout.send_message([0x89, 53, 0])

# set up midi handler
handler = MidiInHandler(midiout)
midiin.set_callback(handler)
