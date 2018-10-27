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

#file = open("record.txt)","a")
#playbackfile = open("record.txt","w")


p = pyaudio.PyAudio()
reader = SimpleMFRC522.SimpleMFRC522()

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

#id,text = reader.read()

continue_reading = True
card_empty = False


# Create an object of the class MFRC522
#MIFAREReader = MFRC522.MFRC522()


def check(fileid):
    datafile = open("record.txt","r")
    for line in datafile:
        if "{0}".format(str(fileid)) in line:
            datafile.close()
            return True
    datafile.close()
    return False

try:
    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
        while continue_reading:
            print("Scan Tag!")
            playbackfile = open("record.txt","r")
        # Scan for cards    
        #(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        #if status == MIFAREReader.MI_OK:
           # print "Card detected"
        
        # Get the UID of the card
        #(status,uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        #if status == MIFAREReader.MI_OK:

            # Print UID
            #print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
        
            # This is the default key for authentication
            #key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
            id,text = reader.read()            
            # Select the scanned tag
            #MIFAREReader.MFRC522_SelectTag(uid)
            #string = "ID: {0}".format(str(id))
            # Authenticate
            #status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
            #print "\n"
    # Check if authenticated
            #if status == MIFAREReader.MI_OK:
            search = "{0}.wav".format(str(id))
            #file.read().find(search)
                #print "The card look like this:"
                # Read block 8
                #if MIFAREReader.MFRC522_Read(8) == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
            #search == "{0}.wav".format(str(id)) 
            #if search in open("record.txt").read():
            #if playbackfile.read(id) == -1:
            if check(id) == False:

                print("\r\r\rnot there")
                #card_empty = True
                playbackfile.close()      
                #continue_reading = False
                recordfile = open("record.txt","a+")
                WAVE_OUTPUT_FILENAME = str(id)+".wav"
                sleep(1)


                print("Recording!")

                frames = []

                for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                    data = stream.read(CHUNK)
                    frames.append(data)

                print("Done!")

                stream.stop_stream()
                stream.close()
                p.terminate()

                wf = wave.open(WAVE_OUTPUT_FILENAME , 'wb')
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))
                recordfile.write("ID: "+str(id)+"\n"+"AudioFile: "+str(id)+".wav"+"\n \n")
                recordfile.close()
     
            else:
                #laybackfile = open("record.txt","a")
                #continue_reading = False
                    # Stop
                   # MIFAREReader.MFRC522_StopCrypto1()
            
                    #Make some sounds
               # if status == MIFAREReader.MI_OK::w
                   #search = "{0}.wav".format(str(id))
                print ("true")
                print("Playing "+search)
                wavObj = sa.WaveObject.from_wave_file(search)
                player = wavObj.play()
                player.wait_done()
                playbackfile.close()
                       
                      # data = MIFAREReader.MFRC522_Read(8)
                       #text = "".join(chr(x) for x in data)
                       #print text
                      # continue_reading = False
            #else:
              #  print "Authentication error"

    #if card_empty:
        
       # name = raw_input("Enter a Card Name:")
       # if len(name)>16:
       #     name=name[:16]
       # data = [ord(x) for x in list(name)]

        #while card_empty:
       # Scan for cards    
        #(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        # If a card is found
        #if status == MIFAREReader.MI_OK:
         #   print "Card detected"
        # Get the UID of the card
        #(status,uid) = MIFAREReader.MFRC522_Anticoll()
        # If we have the UID, continue
        #if status == MIFAREReader.MI_OK:
            # Print UID
        #    print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
        
            # This is the default key for authentication
         #   key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
            
            # Select the scanned tag
          #  MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
           # status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
           # print "\n"
    # Check if authenticated
           # if status == MIFAREReader.MI_OK:

                # Variable for the data to write
    #            data = []

                # Fill the data with 0xFF
            #    for x in range(0,16):
             #       data.append(0xFF)

              #  print "The card looked like this:"
                # Read block 8
               # MIFAREReader.MFRC522_Read(8)
               # print "\n"

                # Write the data
               # MIFAREReader.MFRC522_Write(8, data)
               # print "\n"

             #   print "It now looks like this:"
                # Check to see if it was written
              #  MIFAREReader.MFRC522_Read(8)
               # print "\n"

                # Stop
               # MIFAREReader.MFRC522_StopCrypto1()

                # Make sure to stop reading for cards
            card_empty = False

except KeyboardInterrupt:
    print("Finish!")
    GPIO.cleanup()
    #continue_reading = False
    #file.close()


