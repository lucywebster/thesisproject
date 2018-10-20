import RPi.GPIO as GPIO
import MFRC522
import singal
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

frames = []

continue_reading = True
card_empty = False

file = open(.wav)

MIFAREReader = MFRC522.MFRC522()

while continue_reading:

    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    if status == MIFAREReader.MI_OK
        print "Card detected"

    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    if status == MIFAREReader.MI_OK:

        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

        MIFAREReader.MFRC522_SelectTag(uid)
