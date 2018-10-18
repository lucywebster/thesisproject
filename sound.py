

import sounddevice as sd

duration = 10.5
myrecordin = sd.rec(int(duration * fs), samplerate=fs, channels=2)

sd.wait()


