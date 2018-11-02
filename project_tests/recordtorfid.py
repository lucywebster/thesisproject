
import RPi.GPIO as GPIO
import MFRC522
import signal
import pyaudio
import wave
import SimpleMFRC522
from time import sleep

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)




MIFAREReader = MFRC522.MFRC522()
reader = SimpleMFRC522.SimpleMFRC522()

file = open("record.txt","a")

print("Scan Tag!")

try:
    while True:
            
            id, text = reader.read()
            WAVE_OUTPUT_FILENAME = str(id)+".wav"
            sleep(1)

            print ("recordng!")

            frames = []
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            print("done")

            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(WAVE_OUTPUT_FILENAME , 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            file.write("ID: "+str(id)+"\n"+"AudioFile: "+str(id)+".wav"+"\n")
except KeyboardInterrupt:
            print ("Finish!")
            GPIO.cleanup()
            file.close()

