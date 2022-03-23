# This Python file uses the following encoding: utf-8
"""This file create the different lists for filling the Comboboxes"""

# Global Parameters
# -----------------
ClockStatus = ["Internal", "MIDI Out", "MIDI In", "MIDI In/Out"]
MidiSysExDump = ["Current Program", "Current Bank", "All Banks"]

# Program Parameters
# ------------------

# Oscilator parameters
OscShape = ["Osc off", "Sawtooth", "Triangle", "Saw-Tri", "Pulse xx"]  # pulse xx => where xx = 00 to 99 hoe ga ik dit doen?
# Misc Oscilator parameters
GlideMode = ["FixRate", "FixRate A", "FixTime", "FixTime A"]
KeyAssign = ["Low Note", "LowRetrig", "HighNote", "HighRetrig", "LastNote", "LastRetrig"]

# LFO Parameters
LfoFrequency = ["xxx", "32 Steps", "16 Steps", "8 Steps", "6 Steps", "4 Steps", "3 Steps", "2 Steps", "1.5 Steps", "1 Steps", "2/3 Steps", "1/2 Steps", "1/3 Steps", "1/4 Steps", "1/6 Steps", "1/8 Steps", "16Steps"]  # xxx is frequency from 000 to 150
LfoShape = ["Triangle", "Rev Saw", "Sawtooth", "Square", "Random"]

# Modulation Parameters
ModulationDestinations = ["Off", "Osc 1 Freq",  "Osc 2 Freq", "OscAllFreq", "Osc Mix", "NoiseLevel", "Osc1 PulsW", "Osc2 PulsW", "Osc All PW", "Low Pass", "Resonance", "Audio Mod", "VCA Level", "Output Pan", "LFO 1 Freq", "LFO 2 Freq", "LFO 3 Freq", "LFO 4 Freq", "LFOAllFreq", "LFO 1 Amt", "LFO 2 Amt", "LFO 3 Amt", "LFO 4 Amt", "LFOAll Amt", "Env 1 Amt", "Env 2 Amt", "Env 3 Amt", "EnvAll Amt", "Env1Attack", "Env2Attack", "Env3Attack", "EnvAll Att", "Env1 Decay", "Env2 Decay", "Env3 Decay", "EnvAll Dec", "Env1Releas", "Env2Releas", "Env3Releas", "EnvAll Rel", "Mod 1 Amt", "Mod 2 Amt", "Mod 3 Amt", "Mod 4 Amt", "AudioInVol", "Sub Osc 1", "Sub Osc 2"]
ModelationSources = ["Off", "Sequence1", "Sequence2", "Sequence3", "Sequence4", "LFO 1", "LFO 2", "LFO 3", "LFO 4", "Filt Env1", "VCA Env 2", "Envelope3", "PitchBend", "Mod Wheel", "Pressure", "MidBreath", "Midi Foot", "Midi Exp", "Velocity", "KeyNumber", "Noise", "EnvFollow", "Peak Hold"]

# Push It Switch Parameters
PushMode = ["Normal", "Toggle", "Audio In"]

# Clock Parameters
ClockDivide = ["Half", "Quartr", "Eight", "8 half", "8swing", "8trip", "16th", "16half", "16swng", "16trip", "32nd", "32trip", "64trip"]

# Appregiator Parameters
AppregiatorList = ["Up", "Down", "Up Down", "Assign"]

# Sequence Parameters
SeqTrigger = ["Normal", "No Reset", "No Gate", "NoGateNR", "Key Step", "Audio In"]

# Name Parameter
Name = ""  # name part of file so commenting out here?

# if __name__ == "__main__":
#     pass
