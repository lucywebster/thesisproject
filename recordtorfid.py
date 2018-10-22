#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#

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
WAVE_OUTPUT_FILENAME = "recordtest.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


# Capture SIGINT for cleanup when the script is aborted

# Hook the SIGINT
#signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()
reader = SimpleMFRC522.SimpleMFRC522()
# This loop keeps checking for chips. If one is near it will get the UID and authenticate

file = open("record.txt","a")

print("Scan Tag!")

try:
    while True:
    # Scan for cards    
    #(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    #if status == MIFAREReader.MI_OK:
        #print ("Card detected")
    
    # Get the UID of the card
    #(status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    #if status == MIFAREReader.MI_OK:

        # Print UID
        #print ("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))
    
        # This is the default key for authentication
        #key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        #MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        #status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
        #print "\n"

        # Check if authenticated
        #if status == MIFAREReader.MI_OK:

            # Variable for the data to write
            #data = []

            # Fill the data with 0xFF
            #for x in range(0,16):
                #data.append(0xFF)

            #print "Sector 8 looked like this:"
            # Read block 8
            #print "\n"
            
            id, text = reader.read()
            #file.write(str(id)+"\n")

            sleep(1)

            #print "Sector 8 will now be filled with 0xFF:"
            # Write the data
            #print "\n"

            #print "It now looks like this:"
            # Check to see if it was written
            #MIFAREReader.MFRC522_Read(8)
            print ("recordng!")

            frames = []
            # Fill the data with 0x00
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
            file.write(str(id)+" recordtest.wav"+"\n")
            

            #print "Now we fill it with 0x00:"
            #MIFAREReader.MFRC522_Write(8, sound)
            #print "\n"

            #print "It is now empty:"
            # Check to see if it was written
            #MIFAREReader.MFRC522_Read(8)
            #print "\n"

            # Stop
            #MIFAREReader.MFRC522_StopCrypto1()

            # Make sure to stop reading for cards
except KeyboardInterrupt:
            print ("Finish!")
            GPIO.cleanup()
            file.close()

