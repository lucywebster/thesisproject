#!/usr/bin/env python
#
# The following program has been written by Lucy Webster, 09154752, for the purpose of 
# BEB801 Project, Intergenerational Language Transmission at QUT
#
# The file will allow read and write on to RFID cards

import RPi.GPIO as GPIO
import MFRC522
import signal
import simpleaudio as sa
import pyaudio
import wave
import SimpleMFRC522
from time import sleep

p = pyaudio.PyAudio()
reader = SimpleMFRC522.SimpleMFRC522()
 
CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5


continue_reading = True
card_empty = False

def check(fileid):
    datafile = open("record.txt","r")
    for line in datafile:
        if "{0}".format(str(fileid)) in line:
            datafile.close()
            return True
    datafile.close()
    return False

try:
        while continue_reading:
            print("Scan Tag!")
            wavScan = sa.WaveObject.from_wave_file("beeps/scan.wav")
            player = wavScan.play()
            player.wait_done()

            
            playbackfile = open("record.txt","r")

                  
            id,text = reader.read()            
            search = "{0}.wav".format(str(id))
            if check(id) == False:
                print("not there")
                playbackfile.close()      
                recordfile = open("record.txt","a+")
                WAVE_OUTPUT_FILENAME = str(id)+".wav"
                sleep(1)
                stream = p.open(format=FORMAT,
                                channels=CHANNELS,
                                rate=RATE,
                                input=True,
                                frames_per_buffer=CHUNK)


                print("Recording!")

                wavRec = sa.WaveObject.from_wave_file("beeps/recording.wav")
                player = wavRec.play()
                player.wait_done()

                sleep(1)
            
                frames = []

                for ii in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                    data = stream.read(CHUNK)
                    frames.append(data)

                print("Done!")

                stream.stop_stream()
                stream.close()
               # p.terminate()

                wf = wave.open(WAVE_OUTPUT_FILENAME , 'wb')
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))
                recordfile.write("AudioFile: "+str(id)+".wav"+"\n \n")
                recordfile.close()
     
            else:
                print ("true")
                print("Playing "+search)
                wavObj = sa.WaveObject.from_wave_file(search)
                player = wavObj.play()
                player.wait_done()
                playbackfile.close()

                sleep(1)
            card_empty = False

except KeyboardInterrupt:
    print("Finish!")
    GPIO.cleanup()

