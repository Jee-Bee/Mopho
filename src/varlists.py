# This Python file uses the following encoding: utf-8
"""This file create the different lists for filling the Comboboxes
Warning
-------
Mopho 1.4 software is not added yet!"""

# Global Parameters
# -----------------
ClockStatus = ["Internal", "MIDI Out", "MIDI In", "MIDI In/Out"]
MidiSysExDump = ["Current Program", "Current Bank", "All Banks"]

# Program Parameters
# ------------------

# All Parameters
AllParameters = ["Osc 1 Frequency", "Osc 1 Fine Frequency", "Osc 1 Shape", "Osc 1 Glide",
"Osc 1 Keyboard", "Osc 1 Sub Osc", "Osc 2 Frequency", "Osc 2 Fine Frequency", "Osc 2 Shape",
"Osc 2 Glide", "Osc 2 Keyboard", "Osc 2 Sub Osc", "Sync 2->1", "Glide Mode", "Osc Slop", "PW Range",
"Keyboard Assign", "Osc Mix", "Noise Level", "ExtIn Vol", "Flt Frequency", "Flt Resonance",
"Flt Keyboard Amount", "Flt Audio Mod", "Flt 4-Pole", "Flt Envelope Amount", "Flt Env Velocity",
"Flt Env Delay", "Flt Env Attack","Flt Env Decay", "Flt Env Sustain", "Flt Env Release", "Vca Level",
"Vca Env Amount", "Vca Env Velocity", "Vca Delay", "Vca Env Attack", "Vca Env Decay",
"Vca Env Sustain", "Vca Env Release", "Prog Volume", "Lfo 1 Frequency", "Lfo 1 Shape","Lfo 1 Amount",
"Lfo 1 Destination", "Lfo 1 Key Sync", "Lfo 2 Frequency", "Lfo 2 Shape", "Lfo 2 Amount",
"Lfo 2 Destination", "Lfo 2 Key Sync", "Lfo 3 Frequency", "Lfo 3 Shape", "Lfo 3 Amount",
"Lfo 3 Destination", "Lfo 3 Key Sync", "Lfo 4 Frequency", "Lfo 4 Shape", "Lfo 4 Amount",
"Lfo 4 Destination", "Lfo 4 Key Sync", "Env3 Destination", "Env3 Amount", "Env 3 Env Velocity",
"Env3 Env Delay", "Env3 Env Attack", "Env3 Env Decay", "Env3 Env Sustain", "Env3 Env Release",
"Env3 Repeat", "Mod 1 Source", "Mod 1 Amount", "Mod 1 Destination", "Mod 2 Source", "Mod 2 Amount",
"Mod 2 Destination", "Mod 3 Source", "Mod 3 Amount", "Mod 3 Destination", "Mod 4 Source",
"Mod 4 Amount", "Mod 4 Destination", "ModWheel Amount", "ModWheel Destination", "Press Amount",
"Press Destination", "Breath Amount", "Breath Destination", "Veloc Amount", "Veloc Destination",
"Foot Amount", "Foot Destination", "PushIt Note", "PushIt Velocity", "PushIt Mode", "Clock Bpm",
"Clock Divider", "Arpeggiator Mode", "Arpeggiator On/Off", "Sequencer Trigger", "Sequencer On/Off",
"Sequencer 1 Destination",  "Sequencer 2 Destination", "Sequencer 3 Destination",
"Sequencer 4 Destination", "Sequencer 1 Step 1", "Sequencer 1 Step 2", "Sequencer 1 Step 3",
"Sequencer 1 Step 4", "Sequencer 1 Step 5", "Sequencer 1 Step 6", "Sequencer 1 Step 7",
"Sequencer 1 Step 8", "Sequencer 1 Step 9", "Sequencer 1 Step 10", "Sequencer 1 Step 11",
"Sequencer 1 Step 12", "Sequencer 1 Step 13", "Sequencer 1 Step 14", "Sequencer 1 Step 15",
"Sequencer 1 Step 16", "Sequencer 2 Step 1", "Sequencer 2 Step 2", "Sequencer 2 Step 3",
"Sequencer 2 Step 4", "Sequencer 2 Step 5", "Sequencer 2 Step 6", "Sequencer 2 Step 7",
"Sequencer 2 Step 8", "Sequencer 2 Step 9", "Sequencer 2 Step 10", "Sequencer 2 Step 11",
"Sequencer 2 Step 12", "Sequencer 2 Step 13", "Sequencer 2 Step 14", "Sequencer 2 Step 15",
"Sequencer 2 Step 16", "Sequencer 3 Step 1", "Sequencer 3 Step 2", "Sequencer 3 Step 3",
"Sequencer 3 Step 4", "Sequencer 3 Step 5", "Sequencer 3 Step 6", "Sequencer 3 Step 7",
"Sequencer 3 Step 8", "Sequencer 3 Step 9", "Sequencer 3 Step 10", "Sequencer 3 Step 11",
"Sequencer 3 Step 12", "Sequencer 3 Step 13", "Sequencer 3 Step 14", "Sequencer 3 Step 15",
"Sequencer 3 Step 16", "Sequencer 4 Step 1", "Sequencer 4 Step 2", "Sequencer 4 Step 3",
"Sequencer 4 Step 4", "Sequencer 4 Step 5", "Sequencer 4 Step 6", "Sequencer 4 Step 7",
"Sequencer 4 Step 8", "Sequencer 4 Step 9", "Sequencer 4 Step 10", "Sequencer 4 Step 11",
"Sequencer 4 Step 12", "Sequencer 4 Step 13", "Sequencer 4 Step 14", "Sequencer 4 Step 15",
"Sequencer 4 Step 16"]

# Oscilator parameters
OscShape = ["Osc off", "Sawtooth", "Triangle", "Saw-Tri", "Pulse xx"]  # pulse xx => where xx = 00 to 99 hoe ga ik dit doen?
# Misc Oscilator parameters
GlideMode = ["FixRate", "FixRate A", "FixTime", "FixTime A"]
KeyAssign = ["Low Note", "LowRetrig", "HighNote", "HighRetrig", "LastNote", "LastRetrig"]

# LFO Parameters
LfoFrequency = ["xxx", "32 Steps", "16 Steps", "8 Steps", "6 Steps", "4 Steps","3 Steps", "2 Steps",
"1.5 Steps", "1 Steps", "2/3 Steps", "1/2 Steps", "1/3 Steps", "1/4 Steps", "1/6 Steps",
"1/8 Steps", "16Steps"]  # xxx is frequency from 000 to 150
LfoShape = ["Triangle", "Rev Saw", "Sawtooth", "Square", "Random"]

# Modulation Parameters
ModulationDestinations = ["Off", "Osc 1 Freq",  "Osc 2 Freq", "OscAllFreq", "Osc Mix","NoiseLevel",
"Osc1 PulsW", "Osc2 PulsW", "Osc All PW", "Low Pass", "Resonance", "Audio Mod", "VCA Level",
"Output Pan", "LFO 1 Freq", "LFO 2 Freq", "LFO 3 Freq","LFO 4 Freq", "LFOAllFreq", "LFO 1 Amt",
"LFO 2 Amt", "LFO 3 Amt", "LFO 4 Amt","LFOAll Amt", "Env 1 Amt", "Env 2 Amt", "Env 3 Amt",
"EnvAll Amt", "Env1Attack","Env2Attack", "Env3Attack", "EnvAll Att", "Env1 Decay", "Env2 Decay",
"Env3 Decay", "EnvAll Dec", "Env1Releas", "Env2Releas", "Env3Releas", "EnvAll Rel", "Mod 1 Amt",
"Mod 2 Amt", "Mod 3 Amt", "Mod 4 Amt", "AudioInVol", "Sub Osc 1", "Sub Osc 2"]
ModelationSources = ["Off", "Sequence1", "Sequence2", "Sequence3", "Sequence4", "LFO 1","LFO 2",
"LFO 3", "LFO 4", "Filt Env1", "VCA Env 2", "Envelope3", "PitchBend","Mod Wheel", "Pressure",
"MidBreath", "Midi Foot", "Midi Exp", "Velocity", "KeyNumber", "Noise", "EnvFollow", "Peak Hold"]

# Push It Switch Parameters
PushNote = ["C0", "C#0", "D0", "D#0", "E0", "F0", "F#0", "G0", "G#0", "A1", "A#1", "B1",
"C1", "C#1", "D1", "D#1", "E1", "F1", "F#1", "G1", "G#1", "A2", "A#2", "B2",
"C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A3", "A#3", "B3",
"C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A4", "A#4", "B4",
"C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A5", "A#5", "B5",
"C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A6", "A#6", "B6",
"C6", "C#6", "D6", "D#6", "E6", "F6", "F#6", "G6", "G#6", "A7", "A#7", "B7",
"C7", "C#7", "D7", "D#7", "E7", "F7", "F#7", "G7", "G#7", "A8", "A#8", "B8",
"C8", "C#8", "D8", "D#8", "E8", "F8", "F#8", "G8", "G#8", "A9", "A#9", "B9",
"C9", "C#9", "D9", "D#9", "E9", "F9", "F#9", "G9", "G#9", "A10", "A#10", "B10"]
PushMode = ["Normal", "Toggle", "Audio In"]

# Clock Parameters
ClockDivide = ["Half", "Quartr", "Eight", "8 half", "8swing", "8trip", "16th", "16half",
"16swng", "16trip", "32nd", "32trip", "64trip"]

# Appregiator Parameters
AppregiatorList = ["Up", "Down", "Up Down", "Assign"]

# Sequence Parameters
SeqTrigger = ["Normal", "No Reset", "No Gate", "NoGateNR", "Key Step", "Audio In"]

# Name Parameter
Name = ""  # name part of file so commenting out here?
catagory = ["None", "Keys", "Organs", "Strings", "Soft Lead", "Bright Lead", "Res Lead","Soft Bass",
"Bright Bass", "Res Bass", "Sub Bass", "Brass", "Instruments", "Evolution", "Motion", "Synth",
"Vox", "Bells", "Harmonics", "Sequence", "Percussion", "Noise", "Sound FX", "Pads", "Appreggiator"]  # sound catagory

# if __name__ == "__main__":
#     pass
